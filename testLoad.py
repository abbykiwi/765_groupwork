import pickle
import os
import pyximport; pyximport.install(language_level=3)
from robot import Robot,Light
from seth_controller import SethController, EntityTypes, ENTITY_RADIUS
import math
import numpy as np
from plotting import plot_state_history,fitness_plots,plot_population_genepool

def calculate_penalty(current_pos, step_direction, target_directions):
    angles = []
    for target_direction in target_directions:
        angle = math.atan2(target_direction[1] - current_pos[1], target_direction[0] - current_pos[1])
        angles.append(angle)
    angle_taken = math.atan2(step_direction[1] - current_pos[1], step_direction[0] - current_pos[1])
    closest_val = closest_value(angles,angle_taken)
    penalty = 180 - abs(abs(closest_val - angle_taken) - 180)
    return penalty

def closest_value(angles, angle_taken):
  arr = np.asarray(angles)
  i = (np.abs(arr - angle_taken)).argmin()
  return arr[i]

# for i in range(25):
#     objects = []
#     with (open("Populations/std"+str(i)+".pkl", "rb")) as openfile:
#         while True:
#             try:
#                 objects.append(pickle.load(openfile))
#             except EOFError:
#                 break
#     print(objects)
#     for object in objects:
#         print(object.genome)

# with (open("Populations/10-0.75/generations.pkl", "rb")) as openfile:
#     while True:
#         try:
#             print (pickle.load(openfile))
#         except EOFError:
#             break
def load_file(iteration):
    data = None
    with (open(f"Populations/{iteration}-penalty/fitness_history.pkl", "rb")) as openfile:
        while True:
            try:
                data = np.array(pickle.load(openfile))
            except EOFError:
                break
    return data

import matplotlib.pyplot as plt
savepath = os.path.abspath('./output/')
from pylab import *


# Example usage
# data = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
last_fitnesses = []
fitnesses = []
for i in range(1,11):
    data = load_file(i)
    fitnesses.append(data)
    for j in data:
        last_fitnesses.append(j[len(j)-1])
    #last_fitnesses.append(data[len(data)-1])

plot_fitnesses(fitnesses)

print(last_fitnesses)
print(np.mean(last_fitnesses))
print(np.std(last_fitnesses))
 #
#plt.show()
# visualize_graph(robot)
# print(robot.trial_data['robot'].x_h)
# print()
# print(robot.trial_data['robot'].y_h)
# print()
# print(robot.trial_data['robot'].a_h)
# # from plotting import plot_state_history
# # plot_state_history(os.path.abspath('./output/'), robot, 'test')
# #print(robot.trial_data)
# loss = 0
# for i in range(len(robot.trial_data['robot'].x_h)-1):
#     foods = robot.trial_data['eaten_FOOD_positions']
#     water = robot.trial_data['eaten_WATER_positions']
#     resources = foods+water
#     step = (robot.trial_data['robot'].x_h[i+1], robot.trial_data['robot'].y_h[i+1])
#     current_pos = (robot.trial_data['robot'].x_h[i], robot.trial_data['robot'].y_h[i])
#     loss += calculate_penalty(current_pos,step, resources)
#     print(f"loss ={loss}")