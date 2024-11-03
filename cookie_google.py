from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import time

# Setup Chrome options for existing profile
options = webdriver.ChromeOptions()
options.add_argument(r"C:\Users\Neev\AppData\Local\Google\Chrome\User Data\Default")  # Your profile path
# options.add_argument("profile-directory=Default")  # Or the specific profile you want to use 

# Initialize WebDriver with Service and Options
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open Google Login Page (already logged in manually)
driver.get('https://accounts.google.com')

# Give time to manually verify the login if needed
time.sleep(15)  # Adjust the sleep time to ensure manual login if required

# Save cookies to a file
with open("google_cookies.pkl", "wb") as file:
    pickle.dump(driver.get_cookies(), file)

driver.quit()
print("Cookies saved successfully.")
