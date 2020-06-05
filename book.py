""""
author:nick
description: get picture books from http://www.woaihuiben.com/topics, just for testing
"""
import requests
from bs4 import BeautifulSoup


def get_book_data(url):
    try:
        r = requests.get(url)
        r.encoding = 'utf-8'
        r.raise_for_status
        return r.text
    except:
        return "access failure"


def get_info(content):
    try:
        soup = BeautifulSoup(content, "html.parser")
        names = soup.find_all("p", {"class": "title"})
        img_urls = soup.find_all("img", {"class": "book-thumb"})
        book_data = []
        for i in range(len(names)):

            title = names[i].a.string
            img_url = img_urls[i]['src']
            description = names[i].next_sibling.string

            item = {
                "title": title,
                "img_url": img_url,
                "description": description
            }
            book_data.append(item)

        return book_data
    except:
        return "access failure"


def create_json_file():
    path = "picture_book.json"
    return path


def write_json(path, data):
    # data是list，需要转换成string，才能write
    json_string_data = ','.join(str(i) for i in data)
    with open(path, "w+", encoding="utf-8") as f:
        f.write('[')
        f.write(json_string_data)
        f.write(']')


def main():
    path = create_json_file()
    url = "http://www.woaihuiben.com/topics"
    book_data = get_book_data(url)
    useful_data = get_info(book_data)
    write_json(path, useful_data)


if __name__ == '__main__':
    main()
