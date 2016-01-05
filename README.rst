pyParallel [in development]
============================

Overview
--------
This module encapsulates the access for the parallel port. It provides
backends for Python running on Windows and Linux. Other platforms are
possible too but not yet integrated.

This module is still under development. But it may be useful for
developers.
The Windows version needs a compiled extension and the giveio.sys driver
for Windows NT/2k/XP. It uses ctypes to access functions in a prebuilt DLL.

It is released under a free software license, see LICENSE.txt for more
details.

Copyright (C) 2001-2016 Chris Liechti cliechti@gmx.net

Homepage: https://github.com/pyserial/pyparallel


Features
--------
* same class based interface on all supported platforms
* port numbering starts at zero, no need to know the port name in the
  user program
* port string (device name) can be specified if access through numbering
  is inappropriate


Requirements
------------
* Python 2.2 or newer
* "Java Communications" (JavaComm) extension for Java/Jython


Installation
------------
Extract files from the archive, open a shell/console in that directory and
let Distutils do the rest:

.. code-block:: bash

    $ python setup.py install


Short introduction
------------------

.. code-block:: python

    >>> import parallel
    >>> p = parallel.Parallel()  # open LPT1 or /dev/parport0
    >>> p.setData(0x55)


Examples
--------
Please look in the GIT Repository. There is an example directory where you
can find a simple terminal and more.
https://github.com/pyserial/pyparallel/tree/master/examples


References
----------
* Python: http://www.python.org
* Jython: http://www.jython.org
* Java@IBM http://www-106.ibm.com/developerworks/java/jdk/ (JavaComm
  links are on the download page for the respective platform jdk)
* Java@SUN http://java.sun.com/products/
