import pandas as pd

ages = pd.Series([22, 35, 58, 45, 30])
print(ages)

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [22, 35, 58, 45, 30],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

print(df.sort_values('Age', ascending=False))
df['Senior'] = df['Age'] > 40
print(df)
df2 = pd.read_csv('sample.csv')
print(df2)
print(df2.describe())
print(df2['Salary'].mean())
high_erners = df2[df2['Salary'] > 60000]
print(high_erners)
df2['Level'] = df2['Salary'].apply(lambda x: 'Senior' if x > 60000 else 'Junior')
print(df2)
print(df2.groupby('Level')['Salary'].mean())