import pandas as pd
x = {'estudiante': ['juliana','monica','jose','elizabeth'], 'edad':['18','23','21','24'],'ID': [1,2,3,4], 'pais':['colombia','chile','uruguay','argentina'],'curso':['python', 'excel','HTML','power bi'],
     'calificaciones':[67, 78, 61, 82]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)
#display the result df
df_id = df[['ID']]
print(type(df_id))
z = df[['estudiante', 'edad', 'ID', 'pais', 'curso', 'calificaciones']]
print(z)