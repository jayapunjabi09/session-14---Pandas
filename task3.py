import pandas as pd

data = {
    'match_id': [1, 2, 3, 4, 5],
    'win_by_runs': [20, 0, 15, 0, 0],
    'win_by_wickets': [0, 6, 0, 8, 0]
}

df = pd.DataFrame(data)

def margin_type(row):
    if row['win_by_runs'] > 0:
        return 'Runs'
    elif row['win_by_wickets'] > 0:
        return 'Wickets'
    else:
        return 'Tie/No Result'

df['match_margin_type'] = df.apply(margin_type, axis=1)

print("IPL Match Margin Types:")
print(df)