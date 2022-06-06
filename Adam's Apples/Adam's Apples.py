# # Adam's Apples
# Adam is a farmer who owns an apple orchard. He sells his wares (many varieties of apples) at local farmer's markets.
# However, it's been a particularly bad year for his orchard. It has produced much less fruit than normal.
# Adam believes this is due to the precession of Saturn.
# **As his estranged brother, you help him cut costs!**


# # Exercise #1
# In an attempt to cut costs, Adam is trying to build a robot to automate away his apple-sorting employees' jobs.
# They sort the apples based on how much they can be sold for.
# As his estranged brother, you must help him build him some software to identify how much each apple will sell for
# based on two key characteristics: the size of apple (in cm) and number of blemishes (bruises, worm-bites etc).
# - Each 1cm bigger the apple gets, it should cost **15 cents** more
# - Each extra blemish wipes out (removes) **60 cents** from the price of the apple
# Adam is obsessed with neural networks so insists you build him one, even though it's not necessary.
# Given the following list of `(size, blemish)` tuples called `apple_info`,
# predict the total price of each apple in **dollars** (100 cents in a dollar!)

# In[46]:
apple_info = [(12.7, 0), (11.2, 1), (23.6, 0), (8, 2), (18.76, 3)] # (size, blemish) for each apple
# TODO: You write this bit!
#neural_network_output_prices = [((pair[0]*15 - pair[1]*60) / 100) for pair in apple_info]

# NN(perceptron) for finding the price of  an apple
from random import randint

apples = [(randint(0, 15), randint(0, 5)) for _ in range(200)]
answers = [((apple[0]*15 - apple[1]*60) / 100) for apple in apples]
weights = [0.01, 0.01]

def perceptron(apples, answers, weights):
    predictions = [i for i in range(len(answers))]
    for index, result in enumerate(answers):
        #print(index, result)
        while predictions[index] != result:
            inputs = apples[index]
            predictions[index] = round(inputs[0] * weights[0] + inputs[1] * weights[1], 3)
            print(inputs[0], inputs[1], predictions[index], weights)

            learning_rate = 0.001
            delta = predictions[index] - result
            weights[0] -= learning_rate * delta * inputs[0]
            weights[1] -= learning_rate * delta * inputs[1]
    return predictions

perceptron(apples, answers, weights)
print("\nFinished learning, actual exercise below.\n")
expected_prices = [1.905, 1.08, 3.54, 0.0, 1.014]  # In dollars
neural_network_output_prices = perceptron(apple_info, expected_prices, weights)


assert isinstance(neural_network_output_prices, list), "neural_network_output_prices not a list!"
assert len(neural_network_output_prices) == 5, f"neural_network_output_prices has the wrong number of prices! Should have 5, instead has {len(neural_network_output_prices)}"
assert all(abs(exp_price - nn_price) < 1e-5 for exp_price, nn_price in zip(expected_prices, neural_network_output_prices)),     f"Expected these prices: {expected_prices}, but got these prices: {neural_network_output_prices}"
print("Congratulations! You got it correct. You've done a good deed by helping Adam :)")


# # Exercise #2
# Adam is becoming more and more demanding. Now he wants you to price apples with a neural network like this:
# - The shininess of the apple (measured in lumens reflected from a 10 lumen light) should increase the price by **30 cents** per lumen
# - Each 1cm bigger the apple gets, it should cost **20 cents** more
# - Each extra blemish wipes out (removes) **50 cents** from the price of the apple
# - Each day since picking removes **10 cents** from the price
# - Saturn's level of precession should be involved (but doesn't affect the price!)

# He changes the input to a `numpy` array of `[shininess, size, blemish, days_since_picked, saturn_precession]` called
# `apple_info`. You must again predict the total price of each apple.

# In[20]:
import numpy as np
# [shininess, size, blemish, days_since_picked, saturn_precession] for each apple
apple_info = np.array([
    [6.3, 12.7, 0, 8, 77],
    [0.7, 11.2, 1, 2, -2],
    [3.33, 23.6, 0, 0, -99],
    [2.8, 2.87, 2, 2, 2],
    [18.76, 3, 5, 3, -12]
])
# TODO: You write this bit!
# NN(perceptron) for finding the price of  an apple
from random import randint

apples = np.array([(randint(0, 15), randint(1, 20), randint(0, 5), randint(0, 10), randint(-100, 100)) for _ in range(10000)])
answers = [((apple[0] * 30 + apple[1] * 20 - apple[2] * 50 - apple[3] * 10) / 100) for apple in apples]
weights = [1, 1, 1, 1, 1]


def perceptron(apples, answers, weights):
    predictions = [i for i in range(len(answers))]
    for index, result in enumerate(answers):
        while predictions[index] != result:
            inputs = apples[index]
            prediction = [inputs[index] * weight for index, weight in enumerate(weights)]
            predictions[index] = round(sum(prediction), 3)
            print(index, "\nInputs:", inputs, '\nWeights:', weights, "\nPrediction:", predictions[index], "\nResult:",
                  result)

            learning_rate = 0.00005
            delta = predictions[index] - result
            for num, weight in enumerate(weights):
                weights[num] = weights[num] - learning_rate * delta * inputs[num]

    return predictions


perceptron(apples, answers, weights)
print("\nFinished learning, actual exercise below.\n")

expected_prices = np.array([3.63, 1.75, 5.719, 0.214, 3.428])  # In dollars
neural_network_output_prices = perceptron(apple_info, expected_prices, weights)

assert isinstance(neural_network_output_prices, list), "neural_network_output_prices not a list!"
assert len(neural_network_output_prices) == 5, f"neural_network_output_prices has the wrong number of prices! Should have 5, instead has {len(neural_network_output_prices)}"
assert np.allclose(expected_prices, neural_network_output_prices),     f"Expected these prices: {expected_prices}, but got these prices: {neural_network_output_prices}"
print("Congratulations! You got it correct. You've done a good deed by helping Adam :)")

