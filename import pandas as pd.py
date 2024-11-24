import pandas as pd
x = {'name': ['juliana','monica','jose','elizabeth'], 'ID': [1,2,3,4], 'departamento':['administradora', 'subchef','bartender','auxiliar de cocina'],
     'salario':[2000000, 1500000, 1600000, 1300000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)
#display the result df
df_id = df[['ID']]
print(type(df_id))
z = df[['departamento', 'salario', 'ID']]
print(z)
