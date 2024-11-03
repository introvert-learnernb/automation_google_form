import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime





class Main:
    def __init__(self) -> None:  # Fixed __init__ method name
        self.url = 'https://accounts.google.com/ServiceLogin'
        self.linkedin_url = 'https://www.linkedin.com/login'
        self.forms_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeWTVIqaZMnWHuTqPsVCAchpzKlETeo8x_0PimbGDyeA3WFtQ/viewform'
        self.driver = uc.Chrome(use_subprocess=True)  # Properly create driver instance
   

    def login(self, email, password):
        # Open the URL
        self.driver.get(self.url)

        # Wait for the email field and enter the email
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, 'identifier'))
        ).send_keys(f'{email}\n')
        
        # Wait for the password field and enter the password
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, 'Passwd'))
        ).send_keys(f'{password}\n')

        # Call the code method
        self.code()
      
      
      
                                                                            
    def code(self):
        # Placeholder for any additional actions
        self.driver.get(self.linkedin_url)
        # Locate and enter email and password
        username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
        password_field = self.driver.find_element(By.ID, 'password')
        username_field.send_keys('introvertlearnernb@gmail.com')
        password_field.send_keys('sgZpY,Y=s)m9Z8s')

        # Click the login button
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # Handle potential cookie acceptance button
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept']"))
            )
            cookie_button.click()
        except:
            pass

        # Navigate to 'All Activity' page
        self.driver.get('https://www.linkedin.com/in/neev-badu/recent-activity/all/')

        # Locate the latest post link
        try:
            latest_post_element = WebDriverWait(self.driver, 10).until(
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

         # Open the FORM URL
        self.driver.get(self.forms_url)
        
        time.sleep(3)
        
        # Click the checkbox
        checkbox = self.driver.find_element(By.XPATH, '//*[@role="checkbox"]')
       
        # Wait for a short period to ensure the checkbox action is processed
        date_picker = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='date']"))
        )

        today_date = datetime.now().strftime('%m/%d/%Y')
        
        print(today_date)
        
        # today_button = WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[text()='Today']"))
        # )
        # today_button.click()
        
        time.sleep(1)
        
        email_field = WebDriverWait(self.driver, 20).until(
              EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[1]"))
        )
        
        profile_link = WebDriverWait(self.driver, 20).until(
              EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[2]"))
        )
        
        post_link = WebDriverWait(self.driver, 20).until(
              EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[3]"))
        )
        
        submit_button = WebDriverWait(self.driver, 20).until(
              EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and @aria-label='Submit']"))
        )
        
        email_field.send_keys('introvertlearnernb@gmail.com')
        
        time.sleep(5)
        
        checkbox.click()
        
        time.sleep(5)
        
        profile_link.send_keys('https://www.linkedin.com/in/neev-badu/')
        
        time.sleep(5)
        
        post_link.send_keys(latest_post_link)
        
        time.sleep(5)
        
        date_picker.clear()
        date_picker.send_keys(today_date)
        
        # self.driver.execute_script("arguments[0].value = arguments[1];", date_picker, today_date)
        time.sleep(3)
        
        submit_button.click()
        
        time.sleep(20)
                                                                      
  
                                                                                   
if __name__ == "__main__":
    # Provide your email and password for testing
    email = 'introvertlearnernb@gmail.com'  # Replace with your email
    password = '***************'  # Replace with your password

    # Create an instance of Main and perform the login
    bot = Main()
    bot.login(email, password)
