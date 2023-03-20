# Run examples with Visual Studio Code
## Install Code and Python
* Install Visual Studio Code: https://code.visualstudio.com/download
* Install latest Python: https://www.python.org/downloads/
## Run script
* Open folder containing scripts
* Confirm that you trust the author so the scripts can be run
* Install Python extension 
* Create virtual environment (Ctrl+Shift+P Python: Create Environment)
* Open terminal to install dependencies (Ctrl+Shift+P Terminal: Create New Terminal)
    * Windows: if an error regarding about_Execution_Policies occurs, change default terminal to Command Prompt instead of PowerShell: File -> Preferences -> Settings -> Features -> Terminal -> Integrated -> Default Profile: Windows -> Select `Command Prompt`
    * In terminal: `pip install -r requirements.txt`
    * Windows: Terminal may respond Microsoft C++ Build Tools are required, install using the link. 
    * Windows: If `wordcloud` cannot be installed, try installing wheel from here https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud
* Verify if the scripts contain `Run Cell` options -> Download ipykernel package if prompted
* Select default Python installation to use as kernel
