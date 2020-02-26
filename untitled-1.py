import pickle

open_pickle = open("game_lib.pickle","rb")
show_pickle = pickle.load(open_pickle)
open_pickle.close()

print(show_pickle)
