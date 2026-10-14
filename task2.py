import pandas as pd

data = {
    'match_id': [1, 2, 3, 4, 5],
    'team1': ['CSK', 'MI', 'RCB', 'KKR', 'CSK'],
    'winner': ['CSK', None, 'RCB', 'KKR', None]
}

df = pd.DataFrame(data)

df = df.dropna(subset=['winner'])

df = df.reset_index(drop=True)

print("Cleaned IPL Data:")
print(df)