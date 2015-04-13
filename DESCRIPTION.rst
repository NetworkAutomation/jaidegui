About
------

* Contributors: `Nathan Printz <https://github.com/nprintz>`_ and `Geoff Rhodes <https://github.com/geoffrhodes>`_  
* `Full documentation on Read The Docs <http://jaidegui.readthedocs.org/>`_
* `Jaide Github <https://github.com/NetworkAutomation/jaide>`_  
* `Jaide GUI Github <https://github.com/NetworkAutomation/jaidegui>`_  
* `Pypi Page <https://pypi.python.org/pypi/jaidegui>`_
* `OSX/Windows Compiled Versions <https://github.com/NetworkAutomation/jaidegui/releases/latest>`_  

Description
------------

The ``jaidegui`` package contains is an easy to use GUI that extends the `jaide <http://github.com/NetworkAutomation/jaide>`_ package. The function of Jaide is to augment an engineer's ability to configure or manipulate multiple Junos devices at the same time. A range of functions and use cases are covered. Some features include being able to poll devices for interface errors, grab basic system information, send any operational mode commands, or send and commit a file containing a list of set commands. The Jaide GUI allows the user to easily do these operations through a graphical interface rather than a command line utility. A full list of features and their usage is available in the `documentation <http://jaidegui.readthedocs.org/>`_.  

Jaide, and therefore the CLI tool and the Jaide GUI, leverage several connection types to JunOS devices using python, including: ncclient, paramiko, and scp. With this base of modules, our goal is the ability to perform as many functions that you can do by directly connecting to a device from a remote interface. Since we can do these remotely from one interface, these functions apply rapidly against multiple devices very easily. The CLI tool leverages multiprocessing for handling multiple connections simultaneously. Pushing code and upgrading 20 devices is quite a simple task with the Jaide tool in hand. 

**NOTE** This tool is most beneficial to those who have a basic understanding of JUNOS. This tool can be used to perform several functions against multiple Juniper devices running Junos very easily.  Please understand the ramifications of your actions when using this script before executing it. You can push very significant changes or CPU intensive commands to a lot of devices in the network from one command or GUI execution. This tool should be used with forethought, and we are not responsible for negligence, misuse, time, outages, damages or other repercussions as a result of using this tool.  

Installation
-------------

The **easiest method** to use `jaidegui` is through the compiled versions for Windows and Mac, available on `Github <https://github/NetworkAutomation/jaidegui/releases/latest`_

You can also install `jaidegui` through pip::

	pip install jaidegui

Or by downloading the source code from `github <https://github.com/NetworkAutomation/jaide>`_ and install it manually::

	python setup.py install

If installed manually or through pip instead of the compiled versions, simply use the ``jaidegui`` command in any new terminal window to launch the application. 
