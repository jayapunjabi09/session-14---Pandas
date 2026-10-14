import pandas as pd

matches = pd.DataFrame({
    'match_id': [1, 2, 3, 4, 5],
    'team1': ['CSK', 'MI', 'RCB', 'KKR', 'CSK'],
    'team2': ['MI', 'RCB', 'KKR', 'CSK', 'MI']
})

teams = pd.DataFrame({
    'team': ['CSK', 'MI', 'RCB', 'KKR', 'GT'],
    'city': ['Chennai', 'Mumbai', 'Bengaluru', 'Kolkata', 'Ahmedabad']
})

result = pd.merge(
    matches,
    teams,
    left_on='team1',
    right_on='team',
    how='left'
)

result = result.rename(columns={'city': 'team1_city'})
result = result.drop(columns=['team'])

result = pd.merge(
    result,
    teams,
    left_on='team2',
    right_on='team',
    how='left'
)

result = result.rename(columns={'city': 'team2_city'})
result = result.drop(columns=['team'])

print("IPL Matches with Home Cities:")
print(result)