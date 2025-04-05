# Package Patches for Python 3.13 Compatibility

This document describes the patches applied to external packages to make them compatible with Python 3.13.

## diskcache

File: `.venv/lib/python3.13/site-packages/diskcache/persistent.py`

Changes:
- Updated imports to use collections.abc instead of collections for abstract base classes
- Affected classes: MutableMapping, Sequence, KeysView, ValuesView, ItemsView

## imdbpie

File: `.venv/lib/python3.13/site-packages/imdbpie/auth.py`

Changes:
- Replaced boto with boto3 for AWS authentication
- Updated authentication to use SigV4Auth from botocore
- Removed custom ZuluHmacAuthV3HTTPHandler implementation

## How to Apply Patches

1. Install the packages in your virtual environment:
```bash
pip install -r requirements.txt
```

2. Apply the patches:
```bash
patch .venv/lib/python3.13/site-packages/diskcache/persistent.py < patches/diskcache-persistent.patch
patch .venv/lib/python3.13/site-packages/imdbpie/auth.py < patches/imdbpie-auth.patch
```

These patches are necessary until the upstream packages are updated to support Python 3.13. 