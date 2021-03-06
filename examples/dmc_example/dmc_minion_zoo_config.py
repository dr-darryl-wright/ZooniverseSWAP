import random
from minion_zoo.minion import (ExpertMinion, AllTheSingleLabelsMinion,
                    RandomMinion, NoisyMinion)

class Config(object):

  def __init__(self):
  
    self.annotations = ['N', '1', '2']
    self.workflow_id = 0
    self.metadata    = {'seen_before': False}
    self.classification_file = './minion-zoo-dmc-example-classifications.csv'
    self.gold_file = './minion-zoo-dmc-example-gold-labels.csv'

    names = ['Dave', 'Stuart', 'Jerry', 'Kevin',
             'Tim', 'Mark', 'Phil', 'Carl', 'Josh']

    ids = range(len(names))

    self.minions = [ExpertMinion(0, names[0], self.annotations)]
    for i,name in enumerate(names[1:]):
      confusion_matrix = [1/float(i+1)] * len(self.annotations)
      self.minions.append(NoisyMinion(i+1, name, self.annotations, confusion_matrix))

    self.subjects = [(x,self.annotations.index(random.choice(self.annotations))) for x in range(100)]
