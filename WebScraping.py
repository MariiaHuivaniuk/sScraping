import requests


url = ' https://mof.gov.ua/uk'
response = requests.get(url)
print('Сторінка доступна на сервері') if response.status_code == 200 else print('Сторінка недоступна на сервері')

url = 'https://en.wikipedia.org/robots.txt'
response = requests.get(url)
if response.status_code == 200:
    print(response.text)

