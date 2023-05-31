import csv

def getPlayerMatches(player_name, csv_filename):
    player_name = player_name.title()  # Convert to title case
    matches = []
    
    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['winner_name'] == player_name or row['loser_name'] == player_name:
                match = {'TOURNAMENT': row['tourney_name'], 
                         'DATE': row['tourney_date'],
                         'WINNER': row['winner_name'], 
                         'LOSER': row['loser_name'], 
                         'SCORE': row['score']}
                matches.append(match)
    return matches

# Test cases
matches = getPlayerMatches('Daniil Medvedev', 'atp_matches_2022.csv')
for match in matches:
    print(match)

matches = getPlayerMatches('Novak Djokovic', 'atp_matches_2022.csv')
for match in matches:
    print(match)
