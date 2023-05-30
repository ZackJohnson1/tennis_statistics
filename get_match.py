import csv

def get_match_stats(file_path, tourney_id, match_num):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['tourney_id'] == tourney_id and int(row['match_num']) == match_num:
                winner_stats = {key: val for key, val in row.items() if key.startswith('winner_') or key.startswith('w_')}
                loser_stats = {key: val for key, val in row.items() if key.startswith('loser_') or key.startswith('l_')}
                return winner_stats, loser_stats
    return None, None

#Testing
winner_stats, loser_stats = get_match_stats('atp_matches_2022.csv', '2022-8888', 300)

print("WINNER STATISTICS:\n")
for key, val in winner_stats.items():
    print(f"{key}: {val}")

print("\n-------------------------------------------------------------------")

print("\nLOSER STATISTICS:\n")
for key, val in loser_stats.items():
    print(f"{key}: {val}")
