
import requests
from lxml import html

USERNAME = "5357057661"
PASSWORD = "Shoot4#themoon"

LOGIN_URL = "https://www.powerstream.ca/app/login.jsp"
URL = "https://www.powerstream.ca/app/capricorn?para=index"

def main():
    session_requests = requests.session()

    # Get login csrf token
    # result = session_requests.get(LOGIN_URL)
    # tree = html.fromstring(result.text)
    # authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "accessCode": USERNAME,
        "password2": PASSWORD#,
        # "csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    print result.content

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    print(bucket_names)

if __name__ == '__main__':
    main()