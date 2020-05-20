#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import pandas as pd
import glob
import re


ITEM_CLASS = r"PH-ProductCard-container"
DESCRIPTION_CLASS = r"flex flex-col pl-16"
PRICE_CLASS = r"PH-ProductCard-Total"


def get_df_from_filename(filename):
    soup = BeautifulSoup(open(filename), "html.parser")
    items = []
    for item in soup.find_all('article', {'class' : ITEM_CLASS}):
        tag = item.find('div', {'class': re.compile(DESCRIPTION_CLASS + ".*")})
        items.append([x for x in tag.strings] + [item.find('span', {'class': re.compile(PRICE_CLASS + ".*")}).string])
    df = pd.DataFrame(items)
    df[2] = df[2] + df[3] + df[4]
    df = df[[0,1,2,5]].rename({0: 'Item', 1:'Selling Quantity', 2:'Price per Quantity', 5: 'Price'}, axis = 1)
    return df


def get_csv(htmls, csvs):
    html_files = glob.glob(htmls)
    csv_files = pd.Series(glob.glob(csvs))
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




