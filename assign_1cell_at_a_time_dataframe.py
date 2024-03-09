import pandas as pd

# Create data set.
dataSet = {'Market': ['S&P 500', 'Dow', 'Nikkei'],
           'Last': [2932.05, 26485.01, 21087.16] }

# Create dataframe with data set and named columns.
df1 = pd.DataFrame(dataSet, columns= ['Market', 'Last'])

# Show original DataFrame.
print("\n*** Original DataFrame ***")
print(df1)


dataSet2 = { 'Market': ['Hang Seng', 'DAX'],
             'Last': [26918.58, 11872.44]}
df2 = pd.DataFrame(dataSet2, columns= ['Market', 'Last'])

df1 = df1.append(df2)
print("\n*** Adjusted DataFrame ***")
print(df1)

# Create new column:
df1['New Column'] = 0
print(df1)

# Assign values individually to 3rd column.
COL_NUM = 2
for i in range(0, len(df1)):
    df1.iat[i,COL_NUM] = i + 10
print(df1)

