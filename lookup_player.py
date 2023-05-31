import csv
from datetime import datetime

def getPlayerMatches(player_name, csv_filename):
    player_name = player_name.title()  # Convert to title case
    matches = []
    
    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['winner_name'] == player_name or row['loser_name'] == player_name:
                # Convert date from YYYYMMDD to a more human-readable format
                date = datetime.strptime(row['tourney_date'], '%Y%m%d').strftime('%B %d, %Y')
                match = {'TOURNAMENT': row['tourney_name'], 
                         'DATE': date,
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
