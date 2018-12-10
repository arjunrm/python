import pandas

df1 = pandas.DataFrame([[2, 4, 6],[1, 3, 5]], columns=["Price","Age","Values"])

df2 = pandas.DataFrame([{"Name" : "Jack", "Age" : 40}, {"Name" : "John", "Age" : 23}])

# print(df1)
# print(df2)

# print(df1.mean().mean())

df3 = pandas.read_csv('supermarkets.csv')
# print(df3.set_index("ID"))
# print(df3)

df4 = pandas.read_json('supermarkets.json')
# print(df4.set_index("ID"))
# print(df4)

df5 = pandas.read_excel('supermarkets.xlsx', sheet_name=0)
# print(df5)
# print(df5.iloc[1:5, 3:6])
# print(df5.columns)

# print(df5.shape)
df5["Continent"] = df5.shape[0] * ["North America"]
# print(df5)

df5["Continent"] = df5["Country"] + ',' + "NAR"
# print(df5)

# transpose data frame i.e. rows -> column & column -> row
print(df5.T)


