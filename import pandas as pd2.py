import pandas as pd

x = {'name': ['juliana', 'monica', 'jose', 'elizabeth'], 
     'ID': [1, 2, 3, 4], 
     'departamento': ['administradora', 'subchef', 'bartender', 'auxiliar de cocina'],
     'salario': [2000000, 1500000, 1600000, 1300000]}

# Casting the dictionary to a DataFrame
df = pd.DataFrame(x)

# Display the result df
df_id = df[['ID']]
print(type(df_id))

df_dept_sal_id = df[['departamento', 'salario', 'ID']]
print(df_dept_sal_id)
