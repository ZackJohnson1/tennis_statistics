def get_tournament_statistics(tournament_name, data):
    # Create variables to store the statistics
    num_matches = 0
    most_common_surface = ""
    total_matches_per_round = {}
    top_5_winners = {}
    champion = ""
    finalist = ""
    semifinalists = []
    total_aces = 0

    for row in data:
        # Split the row into individual values
        values = row.split(',')

        # Extract the tournament name from the row
        row_tournament_name = values[1]

        if row_tournament_name == tournament_name:
            # Increment the number of matches
            num_matches += 1

            # Count the occurrences of each surface type
            surface = values[2]
            if surface in total_matches_per_round:
                total_matches_per_round[surface] += 1
            else:
                total_matches_per_round[surface] = 1

            # Count the occurrences of each winner
            winner = values[10]
            if winner in top_5_winners:
                top_5_winners[winner] += 1
            else:
                top_5_winners[winner] = 1

            # Sum up the total ace count for all matches
            w_ace = values[27]
            l_ace = values[44]
            if w_ace:
                total_aces += int(w_ace)
            if l_ace:
                total_aces += int(l_ace)

    if num_matches == 0:
        return "No data available for the specified tournament."

    # Find the most common surface
    most_common_surface = max(total_matches_per_round, key=total_matches_per_round.get)

    # Sort the winners by count in descending order
    top_5_winners = sorted(top_5_winners.items(), key=lambda x: x[1], reverse=True)[:5]

    # Find the champion (player with the most wins)
    champion = top_5_winners[0][0] if top_5_winners else ""

    # Find the finalist (player with the second most wins)
    finalist = top_5_winners[1][0] if len(top_5_winners) > 1 else ""

    # Find the semifinalists (players tied for the third most wins)
    semifinalists = [player[0] for player in top_5_winners[2:4]] if len(top_5_winners) > 3 else []

    # Create a dictionary to store the statistics
    statistics = {
        'Tournament': tournament_name,
        'Number of Matches': num_matches,
        'Most Common Surface': most_common_surface,
        'Total Matches per Surface': total_matches_per_round,
        'Champion': champion,
        'Finalist': finalist,
        'Semifinalists': semifinalists,
        'Total Aces': total_aces,
        'Top 5 Winners': dict(top_5_winners)
    }

    return statistics


def run_test():
    # Read the data from the CSV file
    with open('atp_matches_2022.csv', 'r') as file:
        data = file.readlines()

    # Test case 1: Valid tournament name
    tournament_name = "Atp Cup"
    result = get_tournament_statistics(tournament_name, data)
    print(f"Statistics for tournament: {tournament_name}")
    print(result)
    print()

    # Test case 2: Non-existing tournament name
    tournament_name = "Roland Garros"
    result = get_tournament_statistics(tournament_name, data)
    print(f"Statistics for tournament: {tournament_name}")
    print(result)
    print()


# Run the test
run_test()
