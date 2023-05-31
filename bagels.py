import csv

def find_6_0_sets(player_name):
    sets_6_0 = []
    count = 0

    with open('atp_matches_2022.csv', 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            winner_name = row['winner_name']
            loser_name = row['loser_name']
            score = row['score']
            
            if winner_name == player_name:
                print(f"Match found for {player_name} (win): {score}")
                # Check each set's score in the match
                for set_score in score.split(' '):
                    if set_score.startswith('6-0'):
                        sets_6_0.append(set_score)
                        count += 1
            elif loser_name == player_name:
                print(f"Match found for {player_name} (loss): {score}")
                # Check each set's score in the match
                for set_score in score.split(' '):
                    if set_score.startswith('6-0'):
                        sets_6_0.append(set_score)
                        count += 1
    
    return sets_6_0, count

# Test the function with player name 'Djokovic'
player_name = 'Novak Djokovic'
sets, count = find_6_0_sets(player_name)
print(f"Sets played by {player_name} with a score of 6-0: {sets}")
print(f"Count of 6-0 sets played by {player_name}: {count}")
