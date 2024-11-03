from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Define the scopes required for accessing Google Forms and Google Drive
SCOPES = ['https://www.googleapis.com/auth/forms', 'https://www.googleapis.com/auth/drive']

def authenticate():
    """Authenticate and return the service to interact with Google Forms."""
    creds_file = r"C:\Users\Neev\Downloads\client_secret.json"  # <- Replace with your actual file path
    
    # Set up the flow using OAuth 2.0 client secrets and scopes
    flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
    
    # Run local server flow to authenticate (this will open the user's default browser)
    creds = flow.run_local_server(port=0)
    
    # Initialize the Google Forms API service
    service = build('forms', 'v1', credentials=creds)
    return service

def get_latest_post_link(driver):
    """Log in to LinkedIn and get the latest post link."""
    # Open LinkedIn Login Page
    driver.get('https://www.linkedin.com/login')

    # Locate and enter email and password
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    password_field = driver.find_element(By.ID, 'password')
    username_field.send_keys('introvertlearnernb@gmail.com')
    password_field.send_keys('sgZpY,Y=s)m9Z8s')  # Use environment variables or secure methods to handle passwords

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
        return latest_post_link
    except Exception as e:
        print("Error locating the latest post:", str(e))
        return None

def main():
    # Authenticate and get the Google Forms service
    service = authenticate()

    # Initialize WebDriver with Service and Options
    chrome_binary_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument(r"C:\Users\Neev\AppData\Local\Google\Chrome\User Data\Default")
    options.binary_location = chrome_binary_path
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Get the latest post link from LinkedIn
        latest_post_link = get_latest_post_link(driver)

        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeWTVIqaZMnWHuTqPsVCAchpzKlETeo8x_0PimbGDyeA3WFtQ')
        # Access the Google Form
        form_id = '1FAIpQLSeWTVIqaZMnWHuTqPsVCAchpzKlETeo8x_0PimbGDyeA3WFtQ'
        result = service.forms().get(formId=form_id).execute()
        print("Form Title:", result['info']['title'])

        # You can proceed to fill the form or perform other actions using the latest_post_link

    except Exception as e:
        print("Error during LinkedIn/Google login or form interaction:", str(e))

    finally:
        # Close the browser
        driver.quit()

if __name__ == '__main__':
    main()
