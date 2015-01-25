import sys,math
from player import Player
from table import Table
from game import Game

player_count = int(sys.argv[1])
given_table_count = int(sys.argv[2])
player_per_table = 4

needed_tables = math.floor(player_count / player_per_table)
if needed_tables < given_table_count:
    table_count = needed_tables
else:
    table_count = given_table_count

players_playing = table_count * player_per_table
players_out = player_count - players_playing

Players = []
for p in range(1,player_count + 1):
    Players.append(Player(p))

Tables = []
for p in range(1,table_count + 1):
    Tables.append(Table(p))

game = Game(Tables,Players)
rounds = []
for r in range(1,player_count):
    rounds.append(game.getRound())

round_count = 0
for round in rounds:
    round_count += 1
    print("Round %s" % round_count)
    for table in round.getTables():
        print(table)
        for player in table.getPlayers():
            print(player)
