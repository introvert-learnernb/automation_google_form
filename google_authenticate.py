from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the scopes required for accessing Google Forms and Google Drive
SCOPES = ['https://www.googleapis.com/auth/forms', 'https://www.googleapis.com/auth/drive']

def authenticate():
    """Authenticate and return the service to interact with Google Forms."""
    # Specify the path to your downloaded client secret JSON file
    creds_file = r"C:\Users\Neev\Downloads\client_secret.json"  # <- Replace with your actual file path
    
    # Set up the flow using OAuth 2.0 client secrets and scopes
    flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
    
    # Run local server flow to authenticate (this will open the user's default browser)
    creds = flow.run_local_server(port=0)
    
    # Initialize the Google Forms API service
    service = build('forms', 'v1', credentials=creds)
    return service

def main():
    # Authenticate and get the Google Forms service
    service = authenticate()
    
    # Example: Accessing a Google Form (replace with a valid form ID)
    form_id = '1FAIpQLSeWTVIqaZMnWHuTqPsVCAchpzKlETeo8x_0PimbGDyeA3WFtQ'
    result = service.forms().get(formId=form_id).execute()
    print("Form Title:", result['info']['title'])

if __name__ == '__main__':
    main()
