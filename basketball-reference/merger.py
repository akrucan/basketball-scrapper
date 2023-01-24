from pprint import pprint

import pandas as pd


players = pd.read_json('..\players.json')
salaries = pd.read_json('..\salaries.json')
players = players.groupby(by=['name','year'], axis = 0)
# print(players.filter(lambda x: x.size > 29))
# players.transform(lambda x: x.first() if x.size == 1 else x.to_numpy())

# players.to_json(r'..\players_grouped.json')
#
#
# merged = pd.merge(salaries,players, on=['name','year'])
#
# merged.to_csv(r'..\players_salaries.csv')
