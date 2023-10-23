# Valeria Gamez, vgamez@usc.edu
# ITP 216, Fall 2023
# Section: 32080
# Assignment 9
# Description:
# Extracts information from concert venue HTML file, scraping, stores the webpages locally.
# Prints concert info by venue, by date
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
    file_name = 'sites/fonda.html'
    file_name2 = 'sites/roxy.html'
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
    concerts_at_roxy = dict(zip(dates_list, concert_list))  # dir with all concerts and dates at roxy

    print()
    print('Upcoming shows at The Fonda Theater')
    fonda_list = []
    fonda_dates_list = []
    for date, concert in zip(dates_fonda, concerts_fonda):
        print('\t'+date.text.strip())
        print('\t\t'+concert.text.strip())
        fonda_list.append(concert.text.strip())
        fonda_dates_list.append(date.text.strip())
    concerts_at_fonda = dict(zip(fonda_dates_list, fonda_list))  # contains all concerts and dates at fonda

    # Display all the concerts, irrespective of venue, organized by date.
    # Show the venue name with the show name.
    all_concerts = {}  # creates a dictionary to store all the concerts
    for date, concert in concerts_at_roxy.items():
        if date in all_concerts:  # if the date exists, append the value, with the theater name attached (as a tuple)
            all_concerts[date].append((concert, 'The Roxy Theater'))
        else:  # if the date doesn't exist, create key, add value
            all_concerts[date] = [(concert, 'The Roxy Theater')]

    for date, concert in concerts_at_fonda.items():
        if date in all_concerts:
            all_concerts[date].append((concert, 'The Fonda Theater'))
        else:
            all_concerts[date] = [(concert, 'The Fonda Theater')]

    print()
    print('Concerts by organized by date')
    for date, concert in all_concerts.items():
        print('\t' + date)
        for value in concert:
            print('\t\t' + str(value[0] + ' @ ' + value[1]))


if __name__ == '__main__':
    main()
