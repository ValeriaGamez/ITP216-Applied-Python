# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Homework 9
# Description:
# Code that extracts information from HTML file, scraping, stores the webpages locally.
import os
import ssl
import urllib.request
from bs4 import BeautifulSoup as bs


def get_security_context():
    # Ignore certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def store_webpage(url, ctx, fn):
    page = urllib.request.urlopen(url, context=ctx)
    soup = bs(page.read(), 'html.parser')
    f = open(fn, 'w', encoding='utf-8')
    print(soup, file=f)
    f.close()


def load_webpage(url, ctx):
    page = urllib.request.urlopen(url, context=ctx)
    return bs(page.read(), 'html.parser')


def main():
    ctx = get_security_context()
    web_url = 'https://www.fondatheatre.com/events'
    web_url2 = 'https://www.theroxy.com/events'
    file_name = 'fonda.html'
    file_name2 = 'roxy.html'
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        store_webpage(web_url, ctx, file_name)
    if not os.path.exists(file_name2) or os.path.getsize(file_name2) == 0:
        store_webpage(web_url2, ctx, file_name2)

    file_url = 'file:///' + os.path.abspath(file_name)
    file_url2 = 'file:///' + os.path.abspath(file_name2)
    soup = load_webpage(file_url, ctx)
    soup2 = load_webpage(file_url2, ctx)
    # find all div tags with a class attribute of 'story-wrap'
    # print(soup.find('h3', class_='carousel_item_title_small'))
    dates_fonda = soup.find_all('span', class_='date')
    concerts_fonda = soup.find_all('h3', class_='carousel_item_title_small')

    concert_list = []
    dates_list = []
    print('Upcoming shows at The Roxy Theater')
    concerts2 = soup2.find_all('h3', class_='carousel_item_title_small')
    dates2 = soup2.find_all('span', class_='date')
    for date, concert2 in zip(dates2, concerts2):
        print('\t'+date.text.strip())
        print('\t\t'+concert2.text.strip())
        concert_list.append(concert2.text.strip())
        dates_list.append(date.text.strip())

    print('Upcoming shows at The Fonda Theater')

    for date, concert in zip(dates_fonda, concerts_fonda):
        print('\t'+date.text.strip())
        print('\t\t'+concert.text.strip())
        concert_list.append(concert.text.strip())
        dates_list.append(date.text.strip())

    print(concert_list)
    print(dates_list)

    event_dict = dict(zip(dates_list,concert_list))
    print(event_dict)


if __name__ == '__main__':
    main()
