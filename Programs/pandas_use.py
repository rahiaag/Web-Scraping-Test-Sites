import pandas as pd

# Sample data
data = {
    'Product': ['Phone A', 'Phone B', 'Phone C'],
    'Price': [299, 399, 499],
    'Rating': [4.5, 4.0, 4.8]
}

# Create a DataFrame
df = pd.DataFrame(data)
print(df)