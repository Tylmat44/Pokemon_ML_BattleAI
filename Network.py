import tensorflow as tf

class Network():

    def _init_(self):
        this.model = build_model()
        this.fitness = 0
        this.done = False
        
    def build_model(self):
        model = tf.keras.sequential()
        model.add(tf.keras.layers.Dense(8, input_shape=(4,), bias_initializer='random_uniform', kernel_initializer='random_uniform', activation='relu'))
        model.add(tf.keras.layers.Dense(1, bias_initializer='random_uniform', kernel_initializer='random_uniform', activation='sigmoid'))
        return model

    def set_weights(self, weights1, weights2):
        model.layers[0].set_weights(weights1)
        model.layers[1].set_weights[weights2)

    def get_weights(self):
        return np.array([model.layers[0].get_weights, model.layers[1].get_weights])

    def run_model(self, input):
        val = this.model.predict(input)
        if val > 0 and val <= .25:
            return 0
        elif val > .25 and val <= .5:
            return 1
        elif val > .5 val <= .75:
            return 2
        else:
            return 3

    def calc_fitness(self, ohp, chp, tc):
    	return ohp - chp - tc
    
    def check_done(self, index):
        f = open("COMFILES\\end" + str(index) + ".txt", "r")
		cond = int(f.read())
		f.close()
        
        if cond == 1:
            this.done = True
            return True
        else:
            return False