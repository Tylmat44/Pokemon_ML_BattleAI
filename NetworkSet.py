import tensorflow as tf
import Network as network
import numpy as np

class NetworkSet():

	def _init_(self, size):
		this.population = create_population()
		this.best_fitness = 0
		this.generation = 0
		this.pop_size = size
        this.end = False
        this.crossover_size = int(.4 * this.pop_size)
        this.mutation_rate = .35
        this.mutation_size = int(this.muation_rate * this.pop_size)
        this.random_rate = this.pop_size - (this.crossover_size + this.mutation_size + 1)


	def create_population(self):
		list = []
		for i in range(this.pop_size):
			list.append(network.Network())

		return np.array(list)

	def run_models(self, inputs):
        i = 0
        dcount = 0
        commands = np.empty([this.pop_size])
        for network in this.population:
            if !network.done or !network.check_done(i):
                commands[i] = population.run_model(inputs[i])
            else:
                dcount += 1
            
            if dcount == pop_size:
                this.end = True
            
            i += 1

	def get_fitness(self, end_inputs):
        fitness = [[0 for i in range(2)] for j in range(pop_size)]
        for i in range(pop_size):
            fitness[i][0] = i
            fitness[i][1] = population[i].calc_fitness(end_inputs[1], end_inputs[0], end_inputs[4])
            
        sorted(fitness, key=lambda x : x[1])
        this.best_fitness = fitness[0][1]
        
        return fitness
        
	def evolve(self):

	def mutate(self):

	def breed(self):

	def selection(self):

