import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data = json.loads(response.text)
print('')
print('Дата/Время')
print(data['Date'])
print('')
print(data['Valute']['EUR']['Name'])
print(data['Valute']['EUR']['Value'])
print(data['Valute']['USD']['Name'])
print(data['Valute']['USD']['Value'])
print(data['Valute']['BYN']['Name'])
print(data['Valute']['BYN']['Value'])
print(data['Valute']['UAH']['Name'])
print(data['Valute']['UAH']['Value'])
print(data['Valute']['CHF']['Name'])
print(data['Valute']['CHF']['Value'])