from bs4 import BeautifulSoup
import pandas as pd
import glob

def get_df_from_filename(filename):
    soup = BeautifulSoup(open(filename), "html.parser")
    items = []
    for tag in soup.find_all('div', {'class': 'PH-ProductCard-description flex justify-between'}):
        items.append([x for x in tag.strings])
    df = pd.DataFrame(items)[[0, 1, 2, 3]].rename({0: 'Item', 1:'Selling Quantity', 2:'Price per Quantity', 3: 'Price'}, axis = 1)
    df.to_csv(filename[:-5] + ".csv", index = False)
    return df

html_files = glob.glob('/Users/nvijayakumar/OneDrive/School/College/19 Fall/Misc/Grocery/*.html')
csv_files = pd.Series(glob.glob('/Users/nvijayakumar/OneDrive/School/College/19 Fall/Misc/Grocery/*.csv'))
for html_file in html_files:
    start_index = html_file.rindex('/') + 1
    end_index = html_file.rindex('.')
    file_name = html_file[start_index:end_index]
    if ~(csv_files.str.contains(file_name).any()):
        print('Creating csv from {}.html'.format(file_name))
        get_df_from_filename(html_file)
    else:
        print('{}.csv already exists'.format(file_name))