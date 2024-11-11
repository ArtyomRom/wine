from collections import defaultdict
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas as pd
import argparse


def generate_the_correct_word(year):
    words = ['год', 'года', 'лет']
    remains = year % 100
    if remains in [11, 12, 13, 14]:
        return f'{year} {words[2]}'
    remains = year % 10
    if remains == 1:
        return f'{year} {words[0]}'
    elif remains in [2, 3, 4]:
        return f'{year} {words[1]}'

    return f'{year} {words[2]}'


def main():
    parser = argparse.ArgumentParser(
        description='Главная страница сайта с напитками'
    )
    parser.add_argument('file', help='Введите вашу имя файла и поместите его в директорию')
    parser.add_argument('page_file', help='Введите название страницы')
    args = parser.parse_args()
    parser.print_help()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    excel_wine = pd.read_excel(args.file, sheet_name=args.page_file, na_values=['N/A', 'NA'], keep_default_na=False)
    excel_wine = excel_wine.to_dict(orient='records')
    categories = defaultdict(list)

    for category in excel_wine:
        categories[category['Категория']].append(category)

    rendered = template.render(categories=categories,
                               age_company=generate_the_correct_word(datetime.now().year - 1920))

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
