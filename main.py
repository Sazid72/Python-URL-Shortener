import pyshorteners
from pyshorteners.exceptions import BadURLException, BadAPIResponseException, ShorteningErrorException
s = pyshorteners.Shortener() # Creating shortener object outside avoids creating a new Shortener object on every call

def main():
    user_url = input("Enter your URL: ").strip()
    print(short_url(user_url))

def short_url(url):
    try:
        return (s.tinyurl.short(url))
    except BadURLException:
        return "The provided URL is invalid! Please try again."
    except BadAPIResponseException:
        return "The shortener service didn't respond. Please try again later."
    except ShorteningErrorException:
        return "The third-party API refused or failed to shorten this URL. "
    except Exception as e:
        return f"Unexpected Error: {e}"
if __name__ == '__main__':
    main()
