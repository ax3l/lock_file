This software is in the public domain (there is no license).

~~http://martin.horcicka.eu/python/lock_file/~~


# About this Fork

Since I could not find an active upstream repository nor a working
maintainer contact of [this pip project](https://pypi.python.org/pypi/lock_file)
I published my small patch here.


# Install

```bash
pip install --user git+https://github.com/ax3l/lock_file.git@master
```


# Documentation

From [here](https://pythonhosted.org/lock_file/):

Lock file is a traditional means of synchronization among processes. In this
module it is implemented as an empty regular file exclusively locked using
`fcntl.lockf`. When it is to be released it is removed by default. However,
if all cooperating processes turn off the removal, they get a guaranteed order
of acquisitions and better scalability.

### Class `LockError`

**Parent class:** `Exception`

Raised when a lock file acquisition is unsuccessful because the lock file is
held by another process.

- `__init__(self, message)`
  Initializes the exception.

- `__repr__(self)`
  Returns the official string representation.

### Class `LockFile`

**Parent class:** `object`

This class represents an acquired lock file. After its releasing most methods
lose their sense and raise a ValueError.

- `__init__(self, path, wait = False, remove = True)`
  Creates and locks the specified file. The wait argument can be set to `True` to
  wait until the lock file can be acquired. The remove argument can be set to
  `False` to keep the file after releasing.
  Raises LockError if the wait argument is `False` and the lock file is held by
  another process. Raises `OSError` or `IOError` if any other error occurs. In
  particular, raises `IOError` with the `errno` attribute set to `errno.EINTR`,
  if waiting for the acquisition is interrupted by a signal.

- `__enter__(self)`
  Returns self.
  Raises `ValueError` if the lock file is released.

- `__exit__(self, exc_type, exc_value, traceback)`
  Calls release.
  Raises exceptions raised by release.

- `__repr__(self)`
  Returns the official string representation.

- `fileno(self)`
  Returns the file descriptor used by the lock file.
  Raises `ValueError` if the lock file is released.

- `get_path(self)`
    Returns the path of the lock file.
    Raises `ValueError` if the lock file is released.

- `release(self)`
    Removes (optionally but default) and closes the lock file.
    Raises ValueError if the lock file is already released.
    Raises `OSError` if any other error occurs.

## Examples

Checking if at most one instance of the script is running:

```python
import sys
from lock_file import LockFile, LockError

try:
    lock_f = LockFile('/var/run/app.lock')
except LockError:
    sys.exit('The script is already running')

try:
    do_something_useful()
finally:
    lock_f.release()
```

Waiting for the lock file acquisition:

```python
from lock_file import LockFile

lock_f = LockFile('/var/run/app.lock', wait = True)
try:
    do_something_useful()
finally:
    lock_f.release()
```

Waiting for the lock file acquisition (in Python 2.5 and higher):

```python
from __future__ import with_statement
from lock_file import LockFile

with LockFile('/var/run/app.lock', wait = True):
    do_something_useful()
```

Waiting for a lock of a [h5py](http://www.h5py.org/) file and writing savely
from various processes in parallel:
```python
import h5py as h5

h5_file_name = "example.h5"

lock_f = LockFile(h5_file_name, wait = True, remove = False)
try:
    h5_f = h5.File(h5_file_name, 'a')
    # do something with h5_f object
    h5_f.close()
finally:
    lock_f.release()
```
