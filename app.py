#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import pandas as pd
import glob


def get_price(soup):
    item = soup.find('div', {'class': "PH-ProductCard-Total"})
    return item.find('data')['value'].strip()

def get_description(soup):
    item = soup.find('span', {'class': "PH-ProductCard-item-description"}) 
    return " ".join(item.string.split())

def get_quantity(soup):
    item = soup.find('div', {'class': "PH-ProductCard-Total"})
    return " ".join([i.strip() for i in item.find('span', {'kds-Text--s'}).strings][:3])

def get_selling_quantity(soup):
    item = soup.find('span', {'class': 'kds-Text--xs'})
    return " ".join(item.string.split())

def get_df_from_filename(filename):
    soup = BeautifulSoup(open(filename), "html.parser")
    items = []
    for product in soup.find_all("div", {'class': 'PH-ProductCard-productInfo'}):
        item = {}
        item['Price'] = get_price(product)
        item['Item'] = get_description(product)
        item['Price per Quantity'] = get_quantity(product)
        item['Selling Quantity'] = get_selling_quantity(product)
        items.append(item)
    return pd.DataFrame(items)[['Item', 'Selling Quantity','Price per Quantity', 'Price']]

def get_csv(htmls, csvs):
    html_files = glob.glob(htmls)
    csv_files = pd.Series(glob.glob(csvs), dtype='object')
    for html_file in html_files:
        start_index = html_file.rindex('/') + 1
        end_index = html_file.rindex('.')
        file_name = html_file[start_index:end_index]
        if (len(csv_files) == 0) or (~(csv_files.str.contains(file_name).any())):
            print('Creating csv from {}.html'.format(file_name))
            get_df_from_filename(html_file).to_csv(html_file[:-5] + ".csv", index = False)
        else:
            print('{}.csv already exists'.format(file_name))


htmls = '/Users/nvijayakumar/OneDrive/School/College/Misc/Grocery/*.html'
csvs = '/Users/nvijayakumar/OneDrive/School/College/Misc/Grocery/*.csv'
get_csv(htmls, csvs)

