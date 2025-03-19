from bs4 import BeautifulSoup as bs
import requests

URL = 'https://www.kivano.kg/mobilnye-telefony'

response = requests.get(URL)
html = response.text
soup = bs(html, 'lxml')
telephone_list = soup.find_all('div' , class_='item product_listbox oh')
for phone in telephone_list:
    title = phone.find('div', class_="listbox_title oh").text.strip()
    price = phone.find('div', class_="listbox_price text-center").text.strip()
    photo = phone.find('div',class_="listbox_img pull-left").find('img')
    photo_src = photo['src'] if photo else 'Фото не найдено'
    links = phone.find('a', href=True)
    link_url = links['href'] if links else 'Ссылка не найдена'
print(f"Название: {title}\nЦена: {price}\nФото: {photo_src}\nСсылка: {link_url}\n====")