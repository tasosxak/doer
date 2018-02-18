# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import inspect
import glob,os
import importlib
import string

action_list = []

# Fortwnei ta actions
def load_actions():
    for file in glob.glob(r'actions/*.py'):
        #print file,os.path.basename(file)
        name = os.path.splitext(os.path.basename(file))[0]
        #print "Name: " + name
        if name == "action" or name.startswith("__"): continue
        module = importlib.import_module("actions." + name)
        #print module
        my_class = getattr(module, string.capwords(name))
        #print my_class
        my_instance = my_class()
        action_list.append(my_instance)


#Analuei tin protasi kai ektelei to katallilo action
def analyze(seq):
    action = maxpoint_decision(seq.split(" "))
    if action != None:
        action.doIt()

#Epilegei to action me ta perissotera points
def maxpoint_decision(tokens):
    max_point = -1
    max_action = None
    for action in action_list:
        #print "Action:" + str(action)
        sum_points = 0.0
        words = action.getWords();
        points = action.getPoints();
        for token in tokens:
            if token.lower() in words:
                #print "Match:" + token
                sum_points += points[words.index(token)]
        sum_points /= sum(points)
        #print "Success: " + str(sum_points)
        if sum_points > max_point:
            #print "Choosed: " + str(action)
            max_point = sum_points
            max_action = action

    if max_point < 0.40:
        #print "Rejected: " + str(max_point)
        return None
    #print "Choosed: " + str(max_point)
    return max_action

load_actions()
#print("Action list: " + str(action_list))
