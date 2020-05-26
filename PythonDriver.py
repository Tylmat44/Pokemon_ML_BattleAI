

#f = open("temp.txt", "w")
#f.write("2")

import os
import time
import pandas as pd
import numpy as np

pop_size = 3
inputs = np.empty([pop_size, 5])

i = 0
while i != pop_size:
	f = open("COMFILES\\FILEEND.txt", "w")
	f.write(str(i))
	f.close()
	time.sleep(3)
	os.startfile("C:\\Users\\shado\\OneDrive\\Documents\\Website\\PokemonML\\Pokémon Essentials v17.2 2017-10-15\\Game.exe")
	time.sleep(5)
	i += 1

i = 0
inputs = np.empty([pop_size, 5])
while i != pop_size:
	trigger = 0
	while trigger == 0:
		f = open("COMFILES\\feedCommand" + str(i) + ".txt", "r")
		trigger = int(f.read(1))

	df = pd.read_csv("COMFILES\\in" + str(i) + ".txt")
	inputs[i] = df.to_numpy()
	i += 1

