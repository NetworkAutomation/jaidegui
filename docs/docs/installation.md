Installation and Requirements
=============================

## Compiled Version  

The easiest way to install the Jaide GUI is to download the [compiled version](http://github.com/NetworkAutomation/jaidegui/releases/latest) for your OS (Mac or Windows) and simply run the application. There are no other requirements necessary when using this method, as everything is packaged in with our executable.   

## Via PIP  

You can also install jaidegui through pip

	> pip install jaidegui  

After installing through pip, you have access to the `jaidegui` command in any terminal to start the application.

	> jaidegui  

####  Python Requirements:  

If installing through pip, you must have both [pip](https://pip.pypa.io/en/latest/installing.html) and [python](http://www.python.org/) installed prior to getting `jaidegui`. The Jaide GUI is unfortunately only available on Python version 2.7, due to a required package being Python 2.7 only compatible.

Pip should handle retrieving any necessary requirements, but we list them here for verbosity. The versions of these packages below are the ones that we've tested with.  

[PMW >=1.3.3](http://pmw.sourceforge.net/)  -  http://pmw.sourceforge.net/  
[JAIDE >=2.0.0](https://github.com/NetworkAutomation/jaide)  -  https://github.com/NetworkAutomation/jaide   