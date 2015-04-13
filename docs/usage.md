Basic Jaide GUI Usage  
=====================  

There are two ways to use the Jaide GUI. The easiest is through the [compiled applications](https://github.com/NetworkAutomation/jaidegui/releases/latest) for Windows and Mac. By using the compiled application, you don't need to worry about any python requirements or ever touch the command line. Simply load the application and you're ready to start.  

The other manner is by using the command line to follow the [pip installation instructions](installation.md), and then use the `jaidegui` command in any terminal window.

## Jaide commands  

| Command | Description |  
| ------- | ----------- |  
| Show &#124; Compare | Run a 'show &#124; compare' for a list of set commands. **[1](#notes)** |  
| Device Info | Get basic device information, such as version, model, hostname, serial number, and uptime. |  
| Diff Config | Compare the configuration differences between two devices. |  
| Health Check | Get alarm, CPU, RAM, and temperature status. |  
| Interface Errors | Get any interface errors from any interface. |  
| Operational Command(s) | Send operational command(s) and display the output. **[1](#notes)** Pipes are supported, as well as xpath filtering **[2](#notes).** |  
| SCP Files | Copy files to or from the device(s). |  
| Set Command(s)  | Execute a commit operation. **[1](#notes)** Several options exist for further customization, such as confirming, commit check, comments, etc. |  
| Shell Command(s) | Send shell command(s) and display the output. **[1](#notes)** |  

## Unique functions to the GUI

#### Templates  

Templates are a very useful feature for saving a common scenario for repeated use. Simply set up all the options for an execution of the script, and then choose `File > Save Template` [Ctrl+S] from the menu to save those options to a file. They can then be loaded at a later time using `File > Open Template` [Ctrl+O]. 

**Note -** Passwords are stored in the template in a base64 encoded format. While this is not human readable, it should not be considered fully encrypted nor secure. If you do not want the password stored in this manner simply leave the password field blank when you save the template. 

#### Defaults

A special template called `defaults.ini` can be used to prepopulate the options fields on load. `Set as defaults` from the `File` menu can be used to write the current values to the `defaults.ini` file for future program executions. 

#### Keyboard Shortcuts  

Any of the following keyboard shortcuts can be used to manipulate the GUI:  

| Shortcut | Function | Description |  
| -------- | -------- | ----------- |  
| Ctrl+S | Save Template | Used to save the current status of every option to a template file so it can be loaded later |  
| Ctrl+O | Open Template | Used to open a template file to retrieve the state of each option |  
| Ctrl+F | Clear Fields | Clears all option fields to give yourself a blank slate |  
| Ctrl+W | Clear Output | Clears the output area of all text |  
| Ctrl+R | Run Script | Executes the specified options and runs the script |  
| Ctrl+Q | Quit Jaide GUI | Exits the program |  

### Notes  
* 1) There are multiple ways to specify these pieces of information (Hostnames/IPs, op commands, shell commands, set commands). It can be a single command or IP, multiple in a comma-separated list, or a filepath pointing to a file with one entry on each line.  
* 2) Pipes are very powerful, and should be learned for advanced command usage in [Junos natively](http://www.juniper.net/techpubs/en_US/junos14.2/topics/concept/junos-cli-pipe-filter-functions-overview.html). Xpath filtering is an added feature of Jaide, and can be learned of in our [operational command guide](http://jaide.readthedocs.org/).  