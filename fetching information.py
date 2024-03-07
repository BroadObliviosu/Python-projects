import requests
from bs4 import BeautifulSoup

def fetch_website_content(url):
    try:
        #sending a request to the website
        responce = requests.get(url)

        #checking if the request sent worked
        if responce.status_code == 200:
            #if it worked then it will fetch the HTML code.
            soup = BeautifulSoup(responce.content, 'html.parser')

            #extracting and printing the information from the website.
            title = soup.title.text
            print (f"Title,{title}")

            #printing paragraph
            paragraphs = soup.find_all('p')
            for paragraphs in paragraphs:
                print(paragraphs.text)
    except requests.exceptions.RequestException as e:
        print(f"failed to fetch website. Error: {e}")
    except Exception as e:
        print(f"an unexpected error has occurred: {e}")

url_to_fetch = "https://abcefgs123.com"
fetch_website_content(url_to_fetch)
 # print error message.