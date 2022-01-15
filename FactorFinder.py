import pandas as pd
import numpy as np
from PowerFactorFinder import PowerFactorFinder

class FactorFinder:
  def __init__(self, inputs:[[int]], output:[int], n:int = 5):
    transposed = [list(i) for i in zip(*inputs)]
    return_list = []

    for i in transposed:
      obj = PowerFactorFinder(i, output, n)
      return_list.append(obj)

    self.object_list = return_list

  def getPower(self, n=1):
    return [i.getPower(n) for i in self.object_list]

  def getPowerList(self, n = 1):
    return [i.getPowerList(n) for i in self.object_list]
