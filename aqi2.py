""""
    author:yintengfei
    beatfulsoup
"""
import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyi):
    url = "http://pm25.in/" + city_pinyi
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')

    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_aqi.append((caption, value))
        return city_aqi


def main():
    city_pin_yi = input("input city")
    city_aqi = get_city_aqi(city_pin_yi)
    print("空气质量为：{}".format(city_aqi))


if __name__ == "__main__":
    main()