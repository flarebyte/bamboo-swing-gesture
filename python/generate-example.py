from random import choice, sample, randint
from templating import *

markerColors = "LightGray|DarkGray|Red|Purple|Blue|Green|Brown|Orange|Yellow"

settings = {}
amplitudes = {}
markers = set()

def genSettings(number):
    all = set(enumerationExamples())
    for i in range(1, number):
        selection = set(sample(all, i+1))
        all = all - selection
        settings["s:00"+str(i)]=selection

def genFraction():
    denominator = randint(1, 120)
    numerator = randint(1, denominator)
    return "{}/{}".format(numerator, denominator)

def genFractions(number):
    return [genFraction() for i in range(1, number)]

def genAmplitudes(number):
    for i in range(1, number):
        amplitudes["a:0"+format(i,'02')]= genFractions(number*3)

def genMarker(number):   
    for i in range(number):
        prefix = choice(markerColors.split("|"))
        dots = format(randint(1,99),'02')
        spaces = format(randint(1,99),'02')
        markers.add("{}{}d{}s".format(prefix, dots, spaces))

def genMarkerRuleStatement():
   key = choice(settings.keys())
   value = choice(list(settings[key]))
   return "{} is {}".format(key, value)

def genMarkerRule():
    ands = [genMarkerRuleStatement()]
    if randint(1, 3) == 1:
        ands = ands + [genMarkerRuleStatement()]
    elif randint(1, 4) == 1:
        ands = ands + [genMarkerRuleStatement()]
    return " and ".join(ands)

def genMarkerRules(number):
    results = []
    for i in range(number):
        results = results + [genMarkerRule()]
    return results
