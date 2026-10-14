import pandas as pd

data = {
    'match_id': [1, 2, 3, 4, 5],
    'team1': ['CSK', 'MI', 'RCB', 'CSK', 'KKR'],
    'team2': ['MI', 'RCB', 'KKR', 'RCB', 'MI'],
    'winner': ['CSK', 'MI', 'KKR', 'CSK', 'MI']
}

df = pd.DataFrame(data)

print("First 5 Rows:")
print(df.head())