#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Define the pfSense login URL and credentials
login_url = 'https://pfsense.firewall.com'
username = 'service-py'
password = 'CHANGE_ME'

# Get the current date and time
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Create a session to persist the login
with requests.Session() as session:
    # Get the login page to retrieve the CSRF token
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': '__csrf_magic'})['value']

    # Log in to pfSense with the CSRF token
    login_payload = {
        'usernamefld': username,
        'passwordfld': password,
        '__csrf_magic': csrf_token,
        'login': 'Login'
    }
    response = session.post(login_url, data=login_payload)

    # Check if login was successful
    if 'URL' in response.text:
        print('Login successful')

        # Get the alias update page to retrieve the CSRF token
        alias_update_url = 'https://pfsense.firewall.com/firewall_aliases_edit.php?id=28'
        response = session.get(alias_update_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': '__csrf_magic'})['value']

        # Prepare the alias update data with all required form fields
        alias_data = {
            'name': 'ATTACKERS',  # Alias name
            'descr': f'Updated by script on {current_datetime}',  # Description with current date and time
            'type': 'url',  # Alias type
            'address0': 'https://www.somewhere.com/blacklist.txt',  # Alias URLs
            'address_subnet0': '',  # Subnet (empty for URL type)
            'detail0': 'Blacklist',  # Description for the address
            '__csrf_magic': csrf_token,
            'save': 'Save'  # This may be required to trigger the form submission
        }

        # Update the alias URLs with the CSRF token
        response = session.post(alias_update_url, data=alias_data)
        print("Alias updated successfully")  # Assume success as instructed

        # Get the apply changes page to retrieve the CSRF token
        apply_changes_url = 'https://pfsense.firewall.com/firewall_aliases.php'
        response = session.get(apply_changes_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': '__csrf_magic'})['value']

        # Prepare the form data for applying changes
        apply_changes_data = {
            '__csrf_magic': csrf_token,
            'apply': 'Apply Changes'
        }

        # Debugging: Print form data before making the request
        #print('Apply changes data:', apply_changes_data)

        # Submit the apply changes form
        response = session.post(apply_changes_url, data=apply_changes_data)

        # Check if apply changes was successful
        if 'The changes have been applied successfully' in response.text:
            print('Changes applied successfully')
        else:
            print('Failed to apply changes')
            print(response.text)  # Print the response for debugging
    else:
        print('Login failed')
        print(response.text)  # Print the response for debugging
