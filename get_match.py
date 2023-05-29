def get_match_stats(match_num, tourney_id=None, tourney_name=None):
    with open('atp_matches_2022.csv', 'r') as f:
        header = next(f).strip().split(',')
        for line in f:
            data = line.strip().split(',')
            match_condition = data[header.index('match_num')] == str(match_num)
            tourney_id_condition = True if tourney_id is None else data[header.index('tourney_id')] == tourney_id
            tourney_name_condition = True if tourney_name is None else data[header.index('tourney_name')] == tourney_name
            if match_condition and tourney_id_condition and tourney_name_condition:
                match_data = dict(zip(header, data))
                return '\n'.join(f'{key}: {value}' for key, value in match_data.items())
    return 'No match with such parameters found.'

# Examples of use:
print(get_match_stats(300, tourney_id='2022-8888'))    # by tourney_id
print(" ")
print(get_match_stats(300, tourney_name='Atp Cup'))    # by tourney_name
print(" ")
print(get_match_stats(300, '2022-8888', 'Atp Cup'))    # by both
