import statsapi

# Change start_date and end_date to get the games you want
games = statsapi.schedule(start_date='04/01/2021', end_date='04/01/2021')
for game in games:
    box = statsapi.boxscore_data(game.get('game_id'), timecode=None)
    game['home_batters'] = box.get('homeBatters')
    game['away_batters'] = box.get('awayBatters')
    for x in game['home_batters']:
        if x['personId'] != '0' and x['ab'] != 'AB':
            if int(x['ab']) == 0:
                x['game_ba'] = 'N/A'
            else:
                x['game_ba'] = str(round(int(x['h'])/int(x['ab']), 3))
    for x in game['away_batters']:
        if x['personId'] != '0' and x['ab'] != 'AB':
            if int(x['ab']) == 0:
                x['game_ba'] = 'N/A'
            else:
                x['game_ba'] = str(round(int(x['h'])/int(x['ab']), 3))

    #
    # d_home = box.get('homeBatters')
    # print(d_home)
    # temp = list()
    # for x in d_home:
    #     if x.get('ab').isnumeric():
    #         if 0 < int(x.get('ab')) < 9:
    #             temp.append([d_home[0].get('name').replace(' Batters', ''), 'home', x.get('personId'), x.get('name'), x.get('battingOrder'), x.get('ab'), x.get('h')])
    # print(temp)
    # d_away = box.get('awayBatters')
    # temp = list()
    # for x in d_away:
    #     if x.get('ab').isnumeric():
    #         if 0 < int(x.get('ab')) < 9:
    #             temp.append([d_away[0].get('name').replace(' Batters', ''), 'away', x.get('personId'), x.get('name'), x.get('battingOrder'), x.get('ab'), x.get('h')])
    # print(temp)
