"""Load retained checksum-bound native drawing libraries without online fetches."""
import ctypes
import hashlib
import json
from pathlib import Path
import platform
import tempfile
import zipfile

_HANDLES = []
_ROOT = None


def ensure_linux_libraries():
    global _ROOT
    if platform.system() != 'Linux' or _HANDLES:
        return
    if platform.machine() not in ('x86_64', 'AMD64'):
        raise RuntimeError('Retained drawing runtime supports Linux x86_64 only')
    assets = Path(__file__).resolve().parents[1] / 'assets'
    pin = json.loads((assets / 'native-runtime-pin.json').read_text())
    bundle = assets / 'drawing-libraries.zip'
    if bundle.stat().st_size != pin['size_bytes'] or bundle.stat().st_size > 8 * 1024 * 1024:
        raise RuntimeError('Native runtime archive size differs from release pin')
    raw = bundle.read_bytes()
    if hashlib.sha256(raw).hexdigest() != pin['sha256']:
        raise RuntimeError('Native runtime archive hash differs from release pin')
    _ROOT = tempfile.TemporaryDirectory(prefix='rdkit-native-libraries-')
    root = Path(_ROOT.name)
    with zipfile.ZipFile(bundle) as archive:
        manifest = json.loads(archive.read('manifest.json'))
        expected = {r['path']: r for r in manifest['files']}
        if len(expected) != 18 or set(archive.namelist()) != set(expected) | {'manifest.json'}:
            raise RuntimeError('Unexpected native archive members')
        for name, entry in expected.items():
            if (name.startswith('/') or '..' in Path(name).parts or
                    not name.startswith(('lib/', 'notices/')) or entry['size_bytes'] > 4 * 1024 * 1024):
                raise RuntimeError('Unsafe native archive member')
            data = archive.read(name)
            if len(data) != entry['size_bytes'] or hashlib.sha256(data).hexdigest() != entry['sha256']:
                raise RuntimeError('Native library member differs from manifest')
            target = root / name
            target.parent.mkdir(exist_ok=True)
            target.write_bytes(data)
            target.chmod(0o600)
        for soname in manifest['load_order']:
            if '/' in soname or ('lib/' + soname) not in expected:
                raise RuntimeError('Invalid native load order')
            _HANDLES.append(ctypes.CDLL(str(root / 'lib' / soname), mode=ctypes.RTLD_GLOBAL))
