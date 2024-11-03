from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup the ChromeOptions and Service

chrome_binary_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
options = webdriver.ChromeOptions()
# options.add_argument(r"user-data-dir=C:\Users\Neev\AppData\Local\Google\Chrome for Testing\User Data\Default")
service = Service(ChromeDriverManager().install())
options.binary_location = chrome_binary_path

# Initialize WebDriver with Service and Options
driver = webdriver.Chrome(service=service, options=options)



try:
    # Open LinkedIn Login Page
    driver.get('https://www.linkedin.com/login')

    # Locate and enter email and password
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    password_field = driver.find_element(By.ID, 'password')
    username_field.send_keys('introvertlearnernb@gmail.com')
    password_field.send_keys('sgZpY,Y=s)m9Z8s')

    # Click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Handle potential cookie acceptance button
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept']"))
        )
        cookie_button.click()
    except:
        pass

    # Navigate to 'All Activity' page
    driver.get('https://www.linkedin.com/in/neev-badu/recent-activity/all/')

    # Locate the latest post link
    try:
        latest_post_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'urn:li:activity')]"))
        )
        latest_post_link = latest_post_element.get_attribute('href')

        # Modify link if needed
        if "feed/update" not in latest_post_link:
            activity_id = latest_post_link.split("urn:li:activity:")[-1]
            latest_post_link = f"https://www.linkedin.com/feed/update/urn:li:activity:{activity_id}"

        print("Latest Post Link:", latest_post_link)
    except Exception as e:
        print("Error locating the latest post:", str(e))

   
except Exception as e:
    print("Error during LinkedIn/Google login or form interaction:", str(e))

finally:
    # Close the browser
    driver.quit()
