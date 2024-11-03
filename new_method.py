from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# Setup Firefox profile path
profile_path = r"C:\Users\Neev\AppData\Local\Mozilla\Firefox\Profiles\f7eaa5le.default"
options = webdriver.FirefoxOptions()
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)

# Attach profile to options
options.profile = profile_path

# Set up the service for geckodriver
service = Service(GeckoDriverManager().install())

# Initialize the WebDriver with the specified service and options
driver = webdriver.Firefox(
    service=service,
    options=options
)
