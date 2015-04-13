Windows Compiling  
=================  

For building the windows executable, we had to pre build ('freeze') the Pmw package, so that all parts of it were available to 
py2exe at the time of compilation.  

This means moving the .py files in this folder into the jaidegui package folder, and running the windows compiler (`setup-py2exe.py`) from this location. This operates differently than building the source or py2app versions, which happen one step outside of the `jaidegui` folder.  
