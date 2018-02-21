
import inspect
import glob,os
import importlib
import string
import pyttsx3 as ptsx

action_list = []

# Fortwnei ta actions
def load_actions():
    for file in glob.glob(r'actions/*.py'):
        #print file,os.path.basename(file)
        name = os.path.splitext(os.path.basename(file))[0]
        #print "Name: " + name
        if name in ["action" ,"search"] or name.startswith("__"): continue
        module = importlib.import_module("actions." + name)
        #print module
        my_class = getattr(module, string.capwords(name))
        #print my_class
        my_instance = my_class()
        action_list.append(my_instance)


#Analuei tin protasi kai ektelei to katallilo action
def analyze(seq):
    action,useful_tokens = maxpoint_decision(seq.split(" "))

    if action != None:
        action.doIt(useful_tokens)



#Epilegei to action me ta perissotera points
def maxpoint_decision(tokens):
    max_point = -1
    max_action = None
    max_useful_tokens = []
    for action in action_list:
        print("Action:" + str(action))
        sum_points = 0.0
        useful_tokens = []
        words = list(action.getWords());
        points = list(action.getPoints());
        print(points)
        for token in tokens:
            if token.lower() in words:
                print("Match:" + token)
                sum_points += points[words.index(token.lower())]
                print(sum_points)
            else:
                useful_tokens.append(token.lower())

        print(sum(points))
        sum_points /= sum(points)
        print("Success: " + str(sum_points))
        if sum_points > max_point:
            print("Is max now: " + str(action))
            max_point = sum_points
            max_action = action
            max_useful_tokens = useful_tokens[:]


    if max_point < 0.40:
        print("Rejected: " + str(max_point))
        return None,None
    print("Choosed: " + str(max_point))
    print(max_useful_tokens)
    return max_action,max_useful_tokens

def say(message,speed = 150, lang = 'english'):
    engine.setProperty("rate", speed)
    engine.setProperty('voice',lang)
    engine.say(message)
    engine.runAndWait()

engine = ptsx.init()

load_actions()
print("Action list: " + str(action_list))
