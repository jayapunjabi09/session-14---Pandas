import pandas as pd

data = {
    'match_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'season': [2023, 2023, 2023, 2023, 2023,
               2024, 2024, 2024, 2024, 2024],
    'winner': ['CSK', 'MI', 'CSK', 'RCB', 'MI',
               'CSK', 'KKR', 'MI', 'CSK', 'KKR']
}

df = pd.DataFrame(data)

wins = df.groupby(['season', 'winner']).size()

wins = wins.reset_index(name='total_wins')

top_teams = wins.sort_values(
    by=['season', 'total_wins'],
    ascending=[True, False]
)

top_teams = top_teams.groupby('season').head(3)

print("Top 3 Teams with Most Wins in Each Season:")
print(top_teams)