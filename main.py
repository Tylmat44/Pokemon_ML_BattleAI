import tensorflow as tf
#import Network as network
#import NetworkSet as networkset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import time

pop_size = 3
generation = 0
max_generation
best_fitness = 0
avg_fitness = []
fitness_list = []
commands = []
population = networkset.NetworkSet(pop_size)
inputs = np.empty([pop_size, 5])

def open_sims():
	for i in range(pop_size):
		f = open("COMFILES\\FILEEND.txt", "w")
		f.write(str(i))
		f.close()
		time.sleep(3)
		os.startfile("C:\\Users\\shado\\OneDrive\\Documents\\Website\\PokemonML\\Pokémon Essentials v17.2 2017-10-15\\Game.exe")
		time.sleep(5)
		i += 1
	return

def get_inputs():
	inputs = np.empty([pop_size, 5])
	for i in range(pop_size):
		trigger = 0
		while trigger == 0:
			f = open("COMFILES\\feedCommand" + str(i) + ".txt", "r")
			trigger = int(f.read(1))
			f.close()

		inputs[i] = np.genfromtxt('COMFILES\\in' + str(i) + '.txt', delimiter=',')
		i += 1
	return

def create_files():
	for i in range(pop_size):
		f = open("COMFILES\\doCommand" + str(i) + ".txt", "w")
		f.write(str(7))
		f.close()
		f = open("COMFILES\\end" + str(i) + ".txt", "w")
		f.write(str(0))
		f.close()
	return

def issue_commands():
	for i in range(pop_size):
		f = open("COMFILES\\command" + str(i) + ".txt", "w")
		f.write(commands[i])
		f.close()
		f = open("COMFILES\\doCommand" + str(i) + ".txt", "w")
		f.write(str(0))
		f.close()
	return

def analyze_fitness():

create_files()
open_sims()
while True:
	get_inputs()
	#Returns the suggested commands
	commands = population.run_models(inputs)
	if population.end:
		break()

	issue_commands()

get_inputs()
fitness_list = population.get_fitness(inputs)

analyize_fitness()