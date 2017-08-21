"""Itspaper´s League of Legends Stat Calculator"""

# Module Imports

import IEM as iem
import pickle

# MetaData

__version__ = "Alpha"
__author__ = "Rodrigo 'ItsPaper' Muñoz"
__email__ = "rodrigo.mcuadrada@gmail.com"

# Variable Declarations

pause = iem.pause
clear = iem.cls

# Functions

def get_data():
    try:
        kills = pickle.load(open("Kills.data", "rb"))
        deaths = pickle.load(open("Deaths.data", "rb"))
        assists = pickle.load(open("Assists.data", "rb"))
        creep_score = pickle.load(open("cs.data", "rb"))
        game_result = pickle.load(open("gr.data", "rb"))
        duration = pickle.load(open("duration.data", "rb"))
    except FileNotFoundError:
        kills = []
        deaths = []
        assists = []
        creep_score = []
        game_result = []
        duration = []
        pickle.dump(kills, open("Kills.data", "wb"))
        pickle.dump(deaths, open("Deaths.data", "wb"))
        pickle.dump(assists, open("Assists.data", "wb"))
        pickle.dump(creep_score, open("cs.data", "wb"))
        pickle.dump(game_result, open("gr.data", "wb"))
        pickle.dump(duration, open("duration.data", "wb"))
    finally:
        return kills, deaths, assists, creep_score, game_result, duration


def game_entry(num):
    i = 0
    while i < num:
        try:
            game_kills = int(input("Please enter number of kills"))
            game_deaths = int(input("Please enter number of deaths"))
            game_assists = int(input("Please enter number of assists"))
            game_cs = int(input("Please enter creep score"))
            game_game_result = input("Please Type 'WIN' or 'LOSE'")
            game_duration = int(input("Please enter the number of minutes the game lasted"))
            game_game_result = game_game_result.lower()
            if game_game_result == "win":
                game_game_result = True
            elif game_game_result == "lose":
                game_game_result = False
            else:
                game_game_result = input("Please Type 'WIN' or 'LOSE'")
                game_game_result = game_game_result.lower()
                if game_game_result == "win":
                    game_game_result = True
                elif game_game_result == "lose":
                    game_game_result = False
            kills.append(game_kills)
            deaths.append(game_deaths)
            assists.append(game_assists)
            creep_score.append(game_cs)
            duration.append(game_duration)
            game_result.append(game_game_result)
            pickle.dump(kills, open("Kills.data", "wb"))
            pickle.dump(deaths, open("Deaths.data", "wb"))
            pickle.dump(assists, open("Assists.data", "wb"))
            pickle.dump(creep_score, open("cs.data", "wb"))
            pickle.dump(game_result, open("gr.data", "wb"))
            pickle.dump(duration, open("duration.data", "wb"))
        except:
            print("Game entry Failed")
        finally:
            i += 1


def new_entry():
    games = int(input("How many games will you enter? "))
    game_entry(games)


def read_games():
    i = 1
    n = 0
    for game in kills:
        print("Game Record Number : {}".format(i))
        print("Kills Recorded: {}".format(game))
        print("Deaths Recorded: {}".format(deaths[n]))
        print("Assists Recorded: {}".format(assists[n]))
        print("Creep Score Recorded: {}".format(creep_score[n]))
# Main Code

kills, deaths, assists, creep_score, game_result, duration = get_data()
