import backend
import tkinter as tk
from backend import *
name_of_squad = backend.squad_name()
backend.initialize()
squad = backend.read_squad()
print(name_of_squad)
player_base = backend.player_base

players = backend.random_player_image()

print(players)