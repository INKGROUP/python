""""
    author:yintengfei
"""
import requests


def get_html_text(url):
    r = requests.get(url, timeout=30)
    print(r.status_code)
    return r.text


def main():
    url = "http://qa-m.jianmingzq.com/news/newsDetail"
    content = get_html_text(url)
    print(content)


if __name__ == "__main__":
    main()