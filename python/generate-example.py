from random import choice, sample, randint
from templating import *

markerColors = "LightGray|DarkGray|Red|Purple|Blue|Green|Brown|Orange|Yellow"
amplitudeTransforms = "identity|reverse|invert"
amplitudeSemantic = "Spacing|Jitter|Coloring|Radius|Angle|Distortion|Granularity|Amount|Position|Opacity|Pressure|Scatter|Rotation|Scaling|Size|Smudge|Noise|Flow"
nodeTypes = "0,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,k,q,r,s,t,u,v,w,y,z".upper().split(",")

def genFraction():
    denominator = randint(1, 120)
    numerator = randint(1, denominator)
    return "{}/{}".format(numerator, denominator)

def genFractions(number):
    return [genFraction() for i in range(1, number)]

class BambooGenerator:
    def __init__(self, id):
        self.id = id
        self.settings = {}
        self.amplitudes = {}
        self.markers = set()
        self.markerRules = []
        self.amplitudeRules = []
        self.points = {}

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
        whenConds = "when {} then".format(" and ".join(ands))
        actions = sample(list(self.markers), randint(1,3))
        return {"when": whenConds, "actions": actions}

    def genMarkerRules(self, number):
        results = []
        for i in range(number):
            results = results + [self.genMarkerRule()]
        self.markerRules = results

    def genAmplitudeOneAction(self):
        amplitudeVar = choice(self.amplitudes.keys())
        transformOps = choice("|".split(amplitudeTransforms))
        semantic = choice("|".split(amplitudeSemantic))
        return "{} |> {} |> {}".format(amplitudeVar, transformOps, semantic)

    def genAmplitudeOneRule(self):
        conds = sample(list(self.markers), randint(1,3))
        whenConds = "when {} then".format(" and ".join(conds))
        actions = []
        for i in range(1, randint(1, 3)):
           actions = actions + [self.genAmplitudeOneAction()]
        return {"when": whenConds, "actions": actions}

    def genAmplitudeRules(self, number):
        for i in range(number):
             self.amplitudeRules = self.amplitudeRules + [self.genAmplitudeOneRule()]
    
    def genTranslate(self):
        return "Translate({}, {}, {})".format(choice(self.points.keys()), genFraction(), genFraction())

    def genCircle(self):
        twoPoints = sample(self.points.keys(), 2)
        return "Circle({}, {})".format(choice(self.points.keys()), genFraction())

    def genLine(self):
        twoPoints = sample(self.points.keys(), 2)
        return "Line({}, {})".format(twoPoints[0], twoPoints[1])

    def genBezier(self):
        manyPoints = sample(self.points.keys(), 3)
        return "Bezier({}, {}, {})".format(manyPoints[0], manyPoints[1], manyPoints[2])

    def genBezier2(self):
        manyPoints = sample(self.points.keys(), 4)
        return "Bezier({}, {}, {}, {})".format(manyPoints[0], manyPoints[1], manyPoints[2], manyPoints[3])

    def genPoints(self, zeroTranslateNumber, translateNumber, advancedNumber):
        self.points["p:000"] = "Center"
        for i in range(1, zeroTranslateNumber):
            self.points["p:0"+format(i,'02')] = "nt{}; Translate(p:000, {}, {})".format(choice(nodeTypes),genFraction(), genFraction())

        for i in range(1, translateNumber):
            self.points["p:0"+format(zeroTranslateNumber + i + 1,'02')] = "nt{}; {}".format(choice(nodeTypes), self.genTranslate())

        for i in range(1, advancedNumber):
            transf = sample([self.genLine(), self.genCircle(), self.genBezier(), self.genLine(), self.genCircle(), self.genBezier(), self.genBezier2()], 2)
            self.points["p:0"+format(i+translateNumber + zeroTranslateNumber + 2,'02')] = "nt{}; {} {} |> Inter".format(choice(nodeTypes),transf[0], transf[1])


    def generate(self):
        self.genSettings(randint(4, 9))
        self.genAmplitudes(randint(7, 20))
        self.genMarker(randint(6, 20))
        self.genMarkerRules(randint(3, 20))
        self.genAmplitudeRules(randint(3, 20))
        self.genPoints(randint(10, 20), randint(5, 20), randint(5, 20))



    def display(self):
        print(self.settings)
        print(self.amplitudes)
        print(self.markers)
        print(self.markerRules)
        print(self.amplitudeRules)
        print(self.points)

    def asLines(self):
        lines = header(format(self.id, '02'))
        lines = lines + ['settings: Settings =']
        settingsKeys = self.settings.keys()
        settingsKeys.sort()
        for key in settingsKeys:
           lines = lines + ["    {} := Enum({})".format(key, ", ".join(list(self.settings[key])))]
        
        lines = lines + ['', 'amplitudes: Amplitudes =']
        amplitudeKeys = self.amplitudes.keys()
        amplitudeKeys.sort()
        for key in amplitudeKeys:
           lines = lines + ["    {} := {}".format(key, self.amplitudes[key])]
        
        lines = lines + ['', 'markerRules: MarkerRules =']
        for rule in (self.markerRules):
           lines = lines + ["    {}".format(rule['when'])]
           for action in rule['actions']:
               lines = lines + ["        {}".format(action)]

        lines = lines + ['', 'amplitudeRules: AmplitudeRules =']
        for rule in (self.amplitudeRules):
           lines = lines + ["    {}".format(rule['when'])]
           for action in rule['actions']:
               lines = lines + ["        {}".format(action)]

        lines = lines + ['', 'points: Nodes =']
        pointsKeys = self.points.keys()
        pointsKeys.sort()
        for key in pointsKeys:
           lines = lines + ["    {} := {}".format(key, self.points[key])]

        return lines
    
    def saveAsFile(self):
        with open('examples/sample{}.bambooswing'.format(format(self.id, '02')), 'w') as text_file:
            text_file.writelines(map(lambda x: x + "\n", self.asLines()))

gen = BambooGenerator(1)
gen.generate()
gen.saveAsFile()