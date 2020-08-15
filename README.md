# Grocery Scraper

This is a small script that allows me to digitize Kroger receipts via their website into a `.csv` which is then uploaded to Google Sheets where I can input which items were purchased by who.

## Context
This is the first time I have lived in an apartment with a kitchen, and my roommates and I have began to cook. This involves weekly grocery runs, and we ran into the problem of splitting the grocery bill. It is too much of a hassle to split items at the grocery store itself, as we share many items such as milk, eggs, bread, etc. Manually transcribing the receipts was an option, but seemed inefficient as we purchased 25-30 items a week. Kroger tracks all grocery purchases if you make an account, so I automated the process of scraping and uploading to the receipts to Google Sheets.

The `app.py` file contains code that looks at all the `.html` files in a given directory and provides a `.csv` with the items purchased that week. It then exports the `.csv` with the appropriate filename. The files are uploaded to Google Drive, then when opening the Google Sheet containing all the weekly grocery purchases, new sheets are added based on new `.csv` files that are in the Google Drive folder. The formulas and formatting is autofilled in, so we only have to input the relative proportion for each item (indicated in green in the screenshot) for each person and the totals are listed at the bottom.


This is an example of what the final google sheet looks like after running the contents of `googleAppsScript.js`. The items in green are manually inputed. 


![Google Sheets Screenshot](https://raw.githubusercontent.com/nithvijay/GroceryScraper/master/GoogleSheets.png)
