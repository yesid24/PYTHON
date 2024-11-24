import pandas as pd
# Read the CSV file into a DataFrame
df = pd.read_csv('C:/Users/yesid/OneDrive/Documentos/Investigacion & Estudio/Cursos Coursera/IBM Data Analyst-Coursera/CustomerLoyaltyProgram.csv', header = None)
df.to_excel('C:/Users/yesid/OneDrive/Documentos/Investigacion & Estudio/Cursos Coursera/IBM Data Analyst-Coursera/CustomerLoyaltyProgram123.csv', sheet_name='pag')
print(df.head())

