jupyter nbconvert --to script  GroceryScraperV3.ipynb --TemplateExporter.exclude_input_prompt=True
mv GroceryScraperV3.py app.py
python app.py