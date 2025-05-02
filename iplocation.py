import requests

# IPinfo API kaliti (https://ipinfo.io/signup orqali bepul API kalitini oling)
API_KEY = "3cc21e55fae4a3"

def track_ip(ip_address):
    # API so'rovini yuborish
    url = f"https://ipinfo.io/{ip_address}?token={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"IP Address: {data.get('ip', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Location (Latitude, Longitude): {data.get('loc', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")
    else:
        print(f"Failed to retrieve data for IP: {ip_address}. Status Code: {response.status_code}")

# Terminaldan IP manzilni kiritish
ip_address = input("Enter an IP address (e.g., 192.168.73.24): ")
track_ip(ip_address)