import pandas as pd

# Load CSV data
data = pd.read_csv('Customers.csv')

# Generate insert queries
insert_queries = []
for index, row in data.iterrows():
    values_str = ', '.join([f'"{str(value)}"' for value in row.values])
    insert_query = f'INSERT INTO Customers (CustomerID, Gender, Age, AnnualIncome, SpendingScore, Profession, WorkExperience, FamilySize) VALUES ({values_str});'
    insert_queries.append(insert_query)

# Save insert queries to a file
with open('Insert_Queries.sql', 'w') as f:
    for query in insert_queries:
        f.write(query + '\n')
        
        
