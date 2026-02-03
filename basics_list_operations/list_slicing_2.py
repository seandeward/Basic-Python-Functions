all_players = ['mike', 'ted', 'ashley', 'julie']

def split_players_into_teams(players):
    even_list = players[::2]
    odd_list = players[1::2]
    return even_list, odd_list

print(split_players_into_teams(all_players))