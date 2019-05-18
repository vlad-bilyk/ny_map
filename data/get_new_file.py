from urllib.request import urlopen  # for Python 3: from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
#
# def get_last():
#     URL = 'http://web.mta.info/developers/turnstile.html'
#     soup = BeautifulSoup(urlopen(URL), features="lxml")
#     lst = []
#     for link in soup.find_all('a'):
#         if str(link.get('href')).startswith('data/nyct/turnstile/turnstile_'):
#             lst.append(link.get('href'))
#             if len(lst) == 1:
#                 break
#     return lst

import urllib.request
# from urllib.request import Request, urlopen  # for Python 3: from urllib.request import urlopen
# from bs4 import BeautifulSoup

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def get_last():
    URL = 'http://web.mta.info/developers/turnstile.html'
    opener = AppURLopener()
    response = opener.open(URL)
    soup = response.file.read().decode("utf-8")
    soup = soup.split('\n')
    soup = [i.strip() for i in soup]
    # removing empty elements
    for i in soup:
        if '' in soup:
            soup.remove('')

    # gathering only links
    links = [i for i in soup if i.startswith('<a')]
    links = links[3:]
    links = ''.join(links)
    links = [i for i in links.split('"') if i.startswith('data')]
    latest_link = [links[0]]

    return latest_link

# get_last()
if __name__ == "__main__":
    # print(get_last())
    print(get_last())

    # print(get_last() == get_last1())

