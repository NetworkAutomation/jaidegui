Junos Aide (Jaide) and JGUI  
===========================  

## About  
Contributors: [Geoff Rhodes](https://github.com/geoffrhodes) and [Nathan Printz](https://github.com/nprintz)  
[OSX/Windows Compiled Versions](https://github.com/NetworkAutomation/jaidegui/releases/latest)  
[Read The Docs](http://jaidegui.readthedocs.org/)  
[Jaide GUI Github](https://github.com/NetworkAutomation/jaidegui)  
[Pypi Page](https://pypi.python.org/pypi/jaidegui)  
[Jaide Github](https://github.com/NetworkAutomation/jaide)  

## Table of Contents:
* [About](#about)  
* [Description](#description)  
* [Jaide vs the CLI tool vs the GUI](#jaide-vs-the-cli-tool-vs-the-gui)  
	- [Which is for me?](#which-is-for-me)  
* [Installation](#installation)  
	* [Compiled Versions](#compiled-versions)
	* [Via PIP](#via-pip)
	* [Python Requirements](#python-requirements)  

## Description:

The `jaide` project contains two parts: a library and CLI tool called Jaide, and a GUI wrapper for ease-of-use. This repository is for the GUI wrapper (here called Jaide GUI). The Jaide GUI can be used to manipulate or retrieve information/files/output from one or many devices. Not surprisingly, the CLI tool uses the Jaide class for its internal operations. Some features of Jaide include being able to poll devices for interface errors, grab basic system information, send any operational mode commands, send and commit a file containing a list of set commands, copy files to/from devices, get a configuration diff between two devices, perform a commit check, and run shell commands. A full list of features and their usage is available in the [documentation](http://jaidegui.readthedocs.org/).

Jaide, and therefore the CLI tool and the Jaide GUI, leverage several connection types to JunOS devices using python, including: ncclient, paramiko, and scp. With this base of modules, our goal is the ability to perform as many functions that you can do by directly connecting to a device from a remote interface. Since we can do these remotely from one interface, these functions apply rapidly against multiple devices very easily. The CLI tool leverages multiprocessing for handling multiple connections simultaneously. Pushing code and upgrading 20 devices is quite a simple task with the Jaide tool in hand. 

**NOTE** This tool is most beneficial to those who have a basic understanding of JUNOS. This tool can be used to perform several functions against multiple Juniper devices running Junos very easily.  Please understand the ramifications of your actions when using this script before executing it. You can push very significant changes or CPU intensive commands to a lot of devices in the network from one command or GUI execution. This tool should be used with forethought, and we are not responsible for negligence, misuse, time, outages, damages or other repercussions as a result of using this tool.  

## Jaide vs the CLI tool vs the GUI  

The Jaide project is split into two packages, the `jaide` package, and the `jaidegui` package.  

Currently, the [`jaide` Python package](http://github.com/NetworkAutomation/jaide) includes two things: the Jaide class library for developers, and a CLI tool for network administrators and engineers.  

The `jaidegui` package is a separate Github repository, for ease of change control and management. It includes the GUI and the compiled versions, and can be found [here](https://github.com/NetworkAutomation/jaidegui).  

#### Which is for me?  

 * **Are you wanting to easily manipulate Junos devices using a GUI instead of a CLI, and don't want to worry about Python or programming?**  
 	- We recommend the latest compiled Mac or Windows version of the Jaide GUI available on the [Jaide GUI github page](https://github.com/NetworkAutomation/jaidegui/releases/latest).  

 * **Are you wanting to easily manipulate Junos devices through a CLI tool that can be used on any OS?**  
 	- We recommend following the [pip installation instructions](http://jaide.readthedocs.org/en/latest/installation.html) and using the `jaide` command that is installed into your OS PATH variable. Basic command usage and further specific examples are in the [docs](http://jaide.readthedocs.org/).  


 * **Are you wanting to write python scripts that can manipulate Junos?**  
 	- Follow the [jaide pip installation instructions](http://jaide.readthedocs.org/en/latest/installation.html) and take a look at the Jaide Class Examples section of the [docs](http://jaide.readthedocs.org/).  

 * **Are you wanting to help work on the Jaide project, or just want to take a look under the hood of the CLI tool or Jaide library?**  
 	- [Download](https://github.com/NetworkAutomation/jaide) the source code, and start poking around!

## Installation  

### Compiled Version  

The easiest way to install the Jaide GUI is to download the [compiled version](http://github.com/NetworkAutomation/jaidegui/releases/latest) for your OS (Mac or Windows) and simply run the application. There are no other requirements necessary when using this method, as everything is packaged in with our executable.   

### Via PIP  

You can also install jaidegui through pip

	> pip install jaidegui  

After installing through pip, you have access to the `jaidegui` command in any terminal to start the application.

	> jaidegui  

###  Python Requirements:  

**Only if installing through pip**, you must have both [pip](https://pip.pypa.io/en/latest/installing.html) and [python](http://www.python.org/) installed prior to getting `jaidegui`. The Jaide GUI is unfortunately only available on Python version 2.7, due to a required package being Python 2.7 only compatible.

Pip should handle retrieving any necessary requirements, but we list them here for verbosity. The versions of these packages below are the ones that we've tested with.  

[PMW >=1.3.3](http://pmw.sourceforge.net/)  -  http://pmw.sourceforge.net/  
[JAIDE >=2.0.0](https://github.com/NetworkAutomation/jaide)  -  https://github.com/NetworkAutomation/jaide   
