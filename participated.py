import csv

def check_player_participation(tournament_id=None, tournament_name=None, player_name=None):
    with open('atp_matches_2022.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (tournament_id and row['tourney_id'] == tournament_id) or (tournament_name and row['tourney_name'] == tournament_name):
                if row['winner_name'] == player_name or row['loser_name'] == player_name:
                    return True
        return False


# TESTING WITH ID 
tournament_id = '2022-8888'
player_name = 'Felix Auger Aliassime'

participated = check_player_participation(tournament_id=tournament_id, player_name=player_name)

if participated:
    print(f"The player '{player_name}' participated in the tournament with ID '{tournament_id}'.")
else:
    print(f"The player '{player_name}' did not participate in the tournament with ID '{tournament_id}'.")


#TESTING WITH TOURNEY NAME
tournament_name = 'Atp Cup'
player_name = 'Rafael Nadal'

participated = check_player_participation(tournament_name=tournament_name, player_name=player_name)

if participated:
    print(f"The player '{player_name}' participated in the tournament with name '{tournament_name}'.")
else:
    print(f"The player '{player_name}' did not participate in the tournament with name '{tournament_name}'.")