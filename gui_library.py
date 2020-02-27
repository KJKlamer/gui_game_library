#!/usr/bin/python3
# gui_library
# 02/10/2020
# KJ Klamer
"""This is a gui version of the game library"""
import pickle
import tkinter as tk
from tkinter import scrolledtext
from tkinter import *
class Screen(tk.Frame):
    current = 0  
    

    def __init__(self):
        tk.Frame.__init__(self)
 
    def switch_frame():
        screens[Screen.current].tkraise()
class MainMenu(Screen):
    def __init__(self):
        
        Screen.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "The Game Library", font = ("Ariel", "20"))
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        self.btn_add = tk.Button(self, text = "Add", command = self.go_add)
        self.btn_add.grid(row = 1, column = 0)
        self.btn_edit = tk.Button(self, text = "Edit", command = self.go_edit)
        self.btn_edit.grid(row = 2, column = 0)
        self.btn_search = tk.Button(self, text = "Search")
        self.btn_search.grid(row = 3, column = 0)
        self.btn_remove = tk.Button(self, text = "Remove")
        self.btn_remove.grid(row = 4, column = 0)        
        self.btn_save = tk.Button(self, text = "Save")
        self.btn_save.grid(row = 5, column = 0)
    def go_add(self):
        Screen.current = 2
        Screen.switch_frame()
    def go_edit(self):
        pop_up = tk.Tk()
        pop_up.title("Edit Select")
        frm_edit_select = EditSelect(pop_up)
        frm_edit_select.grid(row = 0, column = 0)
class Search(Screen):
        
    def __init__(self):
        
        Screen.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Search Engine", font = ("Ariel", "20"))
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        self.btn_search_by = tk.Button(self, text = "Search By")
        self.btn_search_by.grid(row = 1, column = 0)
        self.btn_search_for = tk.Button(self, text = "Search For")
        self.btn_search_for.grid(row = 2, column = 0)
        self.btn_search = tk.Button(self, text = "Search")
        self.btn_search.grid(row = 3, column = 0)
        self.btn_remove = tk.Button(self, text = "Remove")
        self.btn_remove.grid(row = 4, column = 0)        
        self.btn_save = tk.Button(self, text = "Save")
        self.btn_save.grid(row = 5, column = 0)   
        
class Add(Screen):
        
    def __init__(self):
        Screen.__init__(self)
        #add title
        self.lbl_title = tk.Label(self, text = "Add a game", font = ("Ariel", "20"))
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        #entry files
        
        #genre
        self.genre_entry = tk.Label(self, text = "Enter the Genre: ")
        self.genre_entry.grid(row = 1, column = 0)
        
        self.ent_genre = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_genre.grid(row = 1, column = 1)
        background = self.ent_genre.cget("bg")      
        #developer
        self.developer_entry = tk.Label(self, text = "Enter the Developer: ")
        self.developer_entry.grid(row = 2, column = 0)
        
        self.ent_developer = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_developer.grid(row = 2, column = 1)
        background = self.ent_developer.cget("bg")
        #year
        self.year_entry = tk.Label(self, text = "Enter the Year it Came Out: ")
        self.year_entry.grid(row = 3, column = 0)
        
        self.ent_year = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_year.grid(row = 3, column = 1)
        background = self.ent_year.cget("bg")         
        #price
        self.price_entry = tk.Label(self, text = "Enter Price of the Game: ")
        self.price_entry.grid(row = 4, column = 0)
        
        self.ent_price = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_price.grid(row = 4, column = 1)
        background = self.ent_price.cget("bg")    
        #title
        self.title_entry = tk.Label(self, text = "Enter the Game Title: ")
        self.title_entry.grid(row = 1, column = 2)
        
        self.ent_title = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_title.grid(row = 1, column = 3)
        background = self.ent_title.cget("bg") 
        #publisher
        self.publisher_entry = tk.Label(self, text = "Enter the Publisher: ")
        self.publisher_entry.grid(row = 2, column = 2)
        
        self.ent_publisher = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_publisher.grid(row = 2, column = 3)
        background = self.ent_publisher.cget("bg")
        #system
        self.system_entry = tk.Label(self, text = "Enter the System it is Run On: ")
        self.system_entry.grid(row = 3, column = 2)
        
        self.ent_system = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_system.grid(row = 3, column = 3)
        background = self.ent_system.cget("bg")
        #rating
        self.rating_entry = tk.Label(self, text = "Enter What you Rate the Game: ")
        self.rating_entry.grid(row = 4, column = 2)
        
        self.ent_rating = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_rating.grid(row = 4, column = 3)
        background = self.ent_rating.cget("bg")
        #space
        self.space_entry = tk.Label(self, text = "")
        self.space_entry.grid(row = 5, column = 0)
        #beat it
        self.beat_it_entry = tk.Label(self, text = "Have you beat it?: ")
        self.beat_it_entry.grid(row = 6, column = 0)
        
        self.btn_yes = tk.Button(self, text = "Yes")
        self.btn_yes.grid(row = 7, column = 0)
        
        self.btn_yes = tk.Button(self, text = "No")
        self.btn_yes.grid(row = 7, column = 1)  
class EditSelect(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        #game drop down
        self.tkvar = tk.StringVar(self)
        self.game_choices = ["Select A Game"]
        for key in range(1, (len(games)+1)):
            contents = games[key]
            self.game_choices.append(contents[1])
        self.tkvar.set(self.game_choices[0])
        self.dbx_games = tk.OptionMenu(self, self.tkvar, *self.game_choices)
        self.dbx_games.grid(row = 0, column = 1, columnspan = 2, sticky = "news")
        #cancel button
        self.btn_cancel = tk.Button(self, text = "Cancel", command = self.parent.destroy)
        self.btn_cancel.grid(row = 1, column = 1)
        #continue button
        self.btn_continue = tk.Button(self, text = "Continue", command = self.continue_to_edit)
        self.btn_continue.grid(row = 1, column = 2)
    def continue_to_edit(self):
        if self.tkvar.get() == self.game_choices[0]:
            self.dbx_games.configure(bg = "red")
        else:
            Screen.current = 3
            Screen.switch_frame()
            for i in range(len(self.game_choices)):
                screens[3].edit_key = i
                break
            screens[3].update()
            self.parent.destroy()

        
class Edit(Screen):
        
    def __init__(self):

        Screen.__init__(self)
        #add title
        self.lbl_title = tk.Label(self, text = "Edit a game", font = ("Ariel", "20"))
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        #entry files
        
        #genre
        self.genre_entry = tk.Label(self, text = "Enter the Genre: ")
        self.genre_entry.grid(row = 1, column = 0)
        
        self.ent_genre = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_genre.grid(row = 1, column = 1)
        background = self.ent_genre.cget("bg")      
        #developer
        self.developer_entry = tk.Label(self, text = "Enter the Developer: ")
        self.developer_entry.grid(row = 2, column = 0)
        
        self.ent_developer = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_developer.grid(row = 2, column = 1)
        background = self.ent_developer.cget("bg")
        #year
        self.year_entry = tk.Label(self, text = "Enter the Year it Came Out: ")
        self.year_entry.grid(row = 3, column = 0)
        
        self.ent_year = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_year.grid(row = 3, column = 1)
        background = self.ent_year.cget("bg")         
        #price
        self.price_entry = tk.Label(self, text = "Enter Price of the Game: ")
        self.price_entry.grid(row = 4, column = 0)
        
        self.ent_price = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_price.grid(row = 4, column = 1)
        background = self.ent_price.cget("bg")    
        #title
        self.title_entry = tk.Label(self, text = "Enter the Game Title: ")
        self.title_entry.grid(row = 1, column = 2)
        
        self.ent_title = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_title.grid(row = 1, column = 3)
        background = self.ent_title.cget("bg") 
        #publisher
        self.publisher_entry = tk.Label(self, text = "Enter the Publisher: ")
        self.publisher_entry.grid(row = 2, column = 2)
        
        self.ent_publisher = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_publisher.grid(row = 2, column = 3)
        background = self.ent_publisher.cget("bg")
        #system
        self.system_entry = tk.Label(self, text = "Enter the System it is Run On: ")
        self.system_entry.grid(row = 3, column = 2)
        
        self.ent_system = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_system.grid(row = 3, column = 3)
        background = self.ent_system.cget("bg")
        #rating
        self.rating_entry = tk.Label(self, text = "Enter What you Rate the Game: ")
        self.rating_entry.grid(row = 4, column = 2)
        
        self.ent_rating = tk.Entry(self, font = ("Ariel", "12"))
        self.ent_rating.grid(row = 4, column = 3)
        background = self.ent_rating.cget("bg")
        #space
        self.space_entry = tk.Label(self, text = "")
        self.space_entry.grid(row = 5, column = 0)
        #beat it
        self.beat_it_entry = tk.Label(self, text = "Have you beat it?: ")
        self.beat_it_entry.grid(row = 6, column = 0)
        
        self.btn_yes = tk.Button(self, text = "Yes")
        self.btn_yes.grid(row = 7, column = 0)
        
        self.btn_yes = tk.Button(self, text = "No")
        self.btn_yes.grid(row = 7, column = 1)
        
        def update(self):
            entry = games[self.edit.keys]
            self.ent_genre.delete(0, "end")
            self.ent_genre.insert(0, entry[0])
        
        def submit_edit(self):
            entry = []
            entry.append(self.ent_genre.get())
            entry.append(self.ent_developer.get())
            entry.append(self.ent_year.get())
            entry.append(self.ent_price.get())    
            entry.append(self.ent_title.get())
            entry.append(self.ent_publisher.get())
            entry.append(self.ent_system.get())
            entry.append(self.ent_rating.get())
            entry.append(self.scr_holes.get())
            games[self.edit_key] = entry
class RemoveSelect(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
#main
if __name__ == "__main__":
    games_library = open("game_lib.pickle","rb")
    games = pickle.load(games_library)
    games_library.close()
    
    
    games = {}
    games_library = open("game_lib.pickle","rb")
    games = pickle.load(games_library)
    games_library.close()  
    
    root = tk.Tk()
    root.geometry("854x480")
    root.title("Gui Library by KJ Klamer")
    main_menu = MainMenu()
    #search_screen = Search()
    #add_game = Add() 
    #edit_game = Edit()
    screens = [MainMenu(),Search(),Add(),Edit()]
    
    screens.append(MainMenu())
    screens.append(Search())
    screens.append(Add())
    screens.append(Edit())
    screens[0].grid(row=0, column = 0, sticky = "news")
    screens[1].grid(row=0, column = 0, sticky = "news")
    screens[2].grid(row=0, column = 0, sticky = "news")
    screens[3].grid(row=0, column = 0, sticky = "news")
    
    Screen.current = 0
    Screen.switch_frame()
    #main_menu.grid(row = 0, column = 0, sticky = "news")
    root.mainloop()