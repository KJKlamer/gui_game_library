#!/usr/bin/python3
# gamelibraryproject.py
# KJ Klamer
# 1/28/2020
import pickle

games = {1:["FPS","Halo 3","Bungie","Microsoft","Xbox 360","2007",
            "6.0","Both","30.00","Yes","1/15/2008","This Game Blows Chunks"],
         2:["Action-Adventure","Just Cause 4","Avalanche Studios","Square Enix",
            "PlayStation 4, Xbox One, Microsoft Windows","2018", "6.0","Singleplayer",
            "40.00", "No", "2/25/2019", "This is actioned packed"]}
data_file = open("game_lib.pickle","wb")
pickle.dump(games, data_file)
data_file.close()

open_pickle = open("game_lib.pickle","rb")
show_pickle = pickle.load(open_pickle)
open_pickle.close()

print(show_pickle)