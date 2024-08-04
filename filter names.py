import pandas as pd

df = pd.read_excel('Dataframes/data.xlsx')
unique_names = df['Name'].drop_duplicates()
unique_names_df = unique_names.to_frame()
unique_names_df.to_excel('unique_attendees.xlsx', index=False)