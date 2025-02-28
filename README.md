# eYePee
IP recon from CLI - scraped from db-ip dot com

Requires requests and beauitfulsoup4

Archlinux users:
pacman -S python-requests python-beautifulsoup4

Others:
pip install requests
pip install beautifulsoup4

# PfSense alias updater
Prelimnary requirements for PFsense firewall:

Create a new user in pfsense called service-py.
Don't make the user admin, instead add the following to the "Effective Priviledges":

WebCfg - Firewall: Alias: Edit	Allow access to the 'Firewall: Alias: Edit' page.	
WebCfg - Firewall: Alias: Import	Allow access to the 'Firewall: Alias: Import' page.	
WebCfg - Firewall: Aliases	Allow access to the 'Firewall: Aliases' page.

Next add a new Alias under the URLs tab, called ATTACKERS and save.

The script should new be able to run and update the ATTACKERS alias.
