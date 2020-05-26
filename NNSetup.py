import tensorflow as tf

class Newtwork():

    def _init_(self):
        this.model=build_model()
        this.fitness = 0
        
    def build_model(self):
        model = tf.keras.sequential()
        model.add(Dense(8, input_shape=(4,), activation='relu'))
        model.add(Dense(4, activation='sigmoid'))
        return model

    def set_weights(self, weights1, weights2):

    def get_weights(self):

    def run_model(self, input):
        

    def calc_fitness(self, ohp, chp, tc):
    	return ohp - chp - tc

    def get_fitness(self):
    	return this.fitness