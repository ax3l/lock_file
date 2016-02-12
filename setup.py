# $Id: setup.py 18 2007-10-24 04:47:12Z horcicka $

from distutils.core import setup

long_description = '''
Lock file is a traditional means of synchronization among processes. In
this module it is implemented as an empty regular file exclusively
locked using fcntl.lockf. When it is to be released it is removed by
default. However, if all cooperating processes turn off the removal,
they get a guaranteed order of acquisitions and better scalability.
'''

setup(
    name='lock_file',
    version='2.0',
    description = 'Lock file manipulation',
    long_description = long_description,
    author = 'Martin Horcicka',
    author_email = 'martin@horcicka.eu',
    url = 'http://martin.horcicka.eu/python/lock_file/',
    download_url
    = 'http://martin.horcicka.eu/python/lock_file/lock_file-2.0.tar.gz',
    py_modules = ['lock_file'],
    license = 'Public Domain',
    platforms = 'Unix-like systems',
    classifiers = [
    'License :: Public Domain',
    'Operating System :: POSIX'])
