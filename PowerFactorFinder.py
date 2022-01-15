import pandas as pd
import numpy as np

class PowerFactorFinder:
  def __init__(self, inputs, outputs, range_ = 5, step = 1):
    arr = inputs
    out = outputs
    d = {}
    
    n = range_

    if 0 in arr:
      index = arr.index(0)
      if index > -1:
        out.pop(index)
        arr.pop(index)

    d["out"] = out

    for i in range(-n, n+1):
      if i == 0:
        continue
      d[i] = []

    for val in arr:
      for i in range(-n, n+1):
        if i == 0:
          continue
        d[i].append(val ** i)

    df = pd.DataFrame(d)

    tempd = dict(df.corr()["out"])
    del tempd["out"]
    t_list = [(i, tempd[i]) for i in tempd]
    func = lambda x : abs(x[1])
    f_list = sorted(t_list, key=func, reverse=True)
    self.power_list = f_list

  def getPowerList(self,n = 1):
    return self.power_list[:min(n, len(self.power_list))]

  def getPower(self,n = 1):
    return [i[0] for i in self.getPowerList(n)]
