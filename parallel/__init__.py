# portable parallel port access with python
# this is a wrapper module for different platform implementations
#
# (C)2001-2002 Chris Liechti <cliechti@gmx.net>
# this is distributed under a free software license, see license.txt

import os
VERSION = "0.3"

# choose an implementation, depending on os
if os.name == 'nt':
    from parallel.parallelwin32 import Parallel  # noqa
elif os.name == 'posix':
    from parallel.parallelppdev import Parallel  # noqa
else:
    raise "Sorry no implementation for your platform available."
