# Run examples with Visual Studio Code
## Install Code and Python
* Install Visual Studio Code: https://code.visualstudio.com/download
* Install latest Python: https://www.python.org/downloads/
## Run script
* Open folder containing scripts
* Confirm that you trust the author so the scripts can be run
* Install Python extension if Code asks
* Create virtual environment (Ctrl+Shift+P Python: Create Environment)
* Open terminal to install dependencies (Ctrl+Shift+P Terminal: Create New Terminal)
    * Windows: if an error regarding about_Execution_Policies occurs, change default terminal to Command Prompt instead of PowerShell: File -> Preferences -> Settings -> Features -> Terminal -> Integrated -> Default Profile: Windows -> Select `Command Prompt`
    * In terminal: `pip install -r requirements.txt`
    * Windows: If `wordcloud` cannot be installed, try installing wheel from here https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud (`pip install wordcloud-1.8.1-cp311-cp311-win_amd64.whl`)
* Replace `hansken_host` variable with the ip of your host 
* Verify if the scripts contain `Run Cell` options -> Download ipykernel package if prompted
* Select default Python installation to use as kernel
