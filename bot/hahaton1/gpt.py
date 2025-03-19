from bs4 import BeautifulSoup as bs
import requests

URL = 'https://www.kivano.kg/mobilnye-telefony'

response = requests.get(URL)
html = response.text
soup = bs(html, 'lxml')

telephone_list = soup.find_all('div', class_='item product_listbox oh')

for phone in telephone_list:
    title = phone.find('div', class_="listbox_title oh").text.strip()  # Убираем лишние пробелы
    price = phone.find('div', class_="listbox_price text-center").text.strip()
    
    # Получаем ссылку на изображение
    photo = phone.find('div', class_="listbox_img pull-left").find('img')
    photo_url = photo['src'] if photo else 'Фото не найдено'
    
    # Получаем ссылку на страницу товара
    link = phone.find('a', href=True)
    link_url = link['href'] if link else 'Ссылка не найдена'
    
    print(f"Название: {title}")
    print(f"Цена: {price}")
    print(f"Фото: {photo_url}")
    print(f"Ссылка: {link_url}")
    print('---')
    