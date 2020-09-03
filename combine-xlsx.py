import pandas as pd
import glob, os

# filenames
excel_names = glob.glob("*.xls")

# read them in
excels = [pd.ExcelFile(name) for name in excel_names]

# turn them into dataframes
frames = [x.parse(x.sheet_names[0], index_col=None) for x in excels]

# concatenate
combined = pd.concat(frames)

# combined.drop_duplicates(subset=[combined.columns[4]], keep = False)

# write it out
writer = pd.ExcelWriter('combined.xlsx', engine='xlsxwriter',options={'strings_to_urls': False, 'header': False, 'index': False})
combined.to_excel(writer)
writer.close()
