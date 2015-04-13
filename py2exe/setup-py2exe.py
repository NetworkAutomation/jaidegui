from distutils.core import setup
import py2exe

setup(
    windows=['Jaide GUI.py'],
    options={
        "py2exe": {
            "bundle_files": 3,
            #"includes": ['jaidegui\jgui_widgets.py', 'jaidegui\module_locator.py', 'jaidegui\worker_thread.py'],
            "packages": ["Pmw", "Crypto", "lxml", "jaide", 'ncclient', 'paramiko', 'scp'],
            "compressed": True
        }
    }
)
