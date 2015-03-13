Description
===========

# TODO: readthedocs link
The `jaidegui` package contains is an easy to use GUI that extends the `jaide` package. The function of Jaide is to augment an engineer's ability to configure or manipulate multiple Junos devices at the same time. A range of functions and use cases are covered. Some features include being able to poll devices for interface errors, grab basic system information, send any operational mode commands, or send and commit a file containing a list of set commands. A full list of features and their usage is available in the [documentation](readthedocs link).  

Jaide, and therfore the Jaide GUI, leverage several connection types to Junos devices using python, including: ncclient, paramiko, and scp. With this base of modules, our goal is the ability to perform as many functions that you can do by directly connecting to a device from a remote interface (in this case, the jaide-gui). Since we can do these remotely from one interface, these functions apply rapidly against multiple devices very easily. The CLI tool leverages multiprocessing for handling multiple connections simultaneously. Pushing code and upgrading 20 devices is quite a simple task with the Jaide tool in hand.  

For information regarding the CLI or base Jaide class, refer to the `jaide` package [located here](https://github.com/NetworkAutomation/jaide).  

**NOTE** This tool is most beneficial to those who have a basic understanding of JUNOS. This tool can be used to perform several functions against multiple Juniper devices running Junos very easily.  Please understand the ramifications of your actions when using this script before executing it. You can push very significant changes or CPU intensive commands to a lot of devices in the network from one command or GUI execution. This tool should be used with forethought, and we are not responsible for negligence, misuse, time, outages, damages or other repercussions as a result of using this tool.  