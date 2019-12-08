from random import choice, sample, randint
from templating import *

markerColors = "LightGray|DarkGray|Red|Purple|Blue|Green|Brown|Orange|Yellow"

def genFraction():
    denominator = randint(1, 120)
    numerator = randint(1, denominator)
    return "{}/{}".format(numerator, denominator)

def genFractions(number):
    return [genFraction() for i in range(1, number)]

class BambooGenerator:
    def __init__(self):
        self.settings = {}
        self.amplitudes = {}
        self.markers = set()
        self.markerRules = []

    def genSettings(self, number):
        all = set(enumerationExamples())
        for i in range(1, number):
            selection = set(sample(all, i+1))
            all = all - selection
            self.settings["s:00"+str(i)]=selection

    def genAmplitudes(self, number):
        for i in range(1, number):
            self.amplitudes["a:0"+format(i,'02')]= genFractions(number*3)

    def genMarker(self, number):   
        for i in range(number):
            prefix = choice(markerColors.split("|"))
            dots = format(randint(1,99),'02')
            spaces = format(randint(1,99),'02')
            self.markers.add("{}{}d{}s".format(prefix, dots, spaces))

    def genMarkerRuleStatement(self):
        key = choice(self.settings.keys())
        value = choice(list(self.settings[key]))
        return "{} is {}".format(key, value)

    def genMarkerRule(self):
        ands = [self.genMarkerRuleStatement()]
        if randint(1, 3) == 1:
            ands = ands + [self.genMarkerRuleStatement()]
        elif randint(1, 4) == 1:
            ands = ands + [self.genMarkerRuleStatement()]
        return " and ".join(ands)

    def genMarkerRules(self, number):
        results = []
        for i in range(number):
            results = results + [self.genMarkerRule()]
        self.markerRules = results
    
    def generate(self):
        self.genSettings(randint(4, 9))
        self.genAmplitudes(randint(7, 20))
        self.genMarker(randint(6, 20))
        self.genMarkerRules(randint(3, 20))


    def display(self):
        print(self.settings)
        print(self.amplitudes)
        print(self.markers)
        print(self.markerRules)


gen = BambooGenerator()
gen.generate()
gen.display()