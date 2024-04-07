import requests
import socks

def fetch_website(url, proxy):
    try:
        session = requests.Session()
        session.proxies = {
            'http': f'socks5://{proxy}',
            'https': f'socks5://{proxy}'
        }
        response = session.get(url)
        if response.status_code == 200:
            print("heres the content of the website:")
            print(response.text)
        else:
            print(f"Failed to fetch website. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    url = input("Enter the URL of the website you want to access: ")
    proxy = input("Enter the SOCKS5 proxy server (Mullvad:, 10.64.0.1:port): ")
    fetch_website(url, proxy)

if __name__ == "__main__":
    main()
