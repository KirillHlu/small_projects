import requests
from bs4 import BeautifulSoup
import flet as ft
from deep_translator import GoogleTranslator

def translate_from(text):
    translated_text = GoogleTranslator(source='auto', target='en').translate(text)
    return translated_text

response = requests.get('https://www.cbr.ru/currency_base/daily/')
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find('table', class_='data').find_all('td')

num_code = []
letter_code = []
unit = []
currency = []
exchange_rate = []
index = 0

try:
    for value in data:
        num_code.append(data[index].text)
        letter_code.append(data[index + 1].text)
        unit.append(data[index + 2].text)
        currency.append(translate_from(str(data[index + 3].text)))
        exchange_rate.append(data[index + 4].text)
        index += 5

except IndexError:
    pass

def main(page: ft.Page):
    table_rows = []
    page.scroll = True
    try:
        for i in range(len(num_code)):
            table_rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(num_code[i])),
                        ft.DataCell(ft.Text(letter_code[i])),
                        ft.DataCell(ft.Text(unit[i])),
                        ft.DataCell(ft.Text(currency[i])),
                        ft.DataCell(ft.Text(f'{exchange_rate[i]} (RUB)')),
                    ]
                )
            )
    except IndexError:
        pass

    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("num_code")),
                ft.DataColumn(ft.Text("letter_code")),
                ft.DataColumn(ft.Text("unit")),
                ft.DataColumn(ft.Text("currency")),
                ft.DataColumn(ft.Text("exchange_rate")),
            ],
            rows=table_rows,
        )
    )

ft.app(target=main)
