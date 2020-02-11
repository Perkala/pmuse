# pmuse
Downloads songs from youtubes playlist in mp3 format using headless chrome with selenium.

# Installation
Clone the repository and install requirements via:
```
pip install -r requirements.txt
```
Suggested usage with some of the python virtual environments.

# Usage
After navigating to repository path execute main.py as following:
```
python main.py [-d DESTINATION] [cdp PATH] playlist_url
```
Destination **-d** and ChromeDriver path **-cdp** are optional arguments.  
If you don't provide **-d**, downloads will be placed in directory set by automated chrome.  
If you don't want to provide **-cdp** every time you run the script you can put it directly into *selenium_automation_script* in *initalize_driver* function.  






