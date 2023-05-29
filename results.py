import csv

def search_player_results(tourney_id, player_name):
    results = []

    with open('atp_matches_2022.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['tourney_id'] == tourney_id:
                if row['winner_name'] == player_name:
                    result = f"{row['winner_name']} def {row['loser_name']}: {row['score']}"
                    results.append(result)
                elif row['loser_name'] == player_name:
                    result = f"{row['winner_name']} def {row['loser_name']}: {row['score']}"
                    results.append(result)

    return results


# Testing
tournament_id = '2022-8888'
player = 'Felix Auger Aliassime'

player_results = search_player_results(tournament_id, player)
for result in player_results:
    print(result)
