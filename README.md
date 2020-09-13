# Framework features
- Page object design
- Base page
  - Provides wrapper over common selenium actions
  - Each page defines an identifier element, after navigating to the page checks if the identifier element is displayed  - acts as assurance that page is loaded, you are on the right page
  - Each PO returns new PO or self
- Custom cmd arguments to pass browser, headless mode, env, URL
- Custom logging
- Customized reporting
- Utils library
- Configurability


##How to run
1. cd to root folder
2. run command: pytest tests


# Versions


##Selenium 
  
Version: 3.141.0


##Chrome 

Source: https://chromedriver.chromium.org/  
Version: ChromeDriver v85.0.4183.87

##Firefox

Source: https://github.com/mozilla/geckodriver/releases/tag/v0.27.0  
Version: Geckodriver v0.27.0  


##Setup venv and install requirement

python3 -m venv venv 

source venv/bin/activate

pip install -r requirements.txt



