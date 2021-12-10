import numpy as np
import matplotlib.font_manager as font_manager
from matplotlib import rcParams
from math import log
from scipy import stats
import re
rcParams['mathtext.default'] = 'regular'



data = np.loadtxt('model.csv',dtype=np.str,delimiter=',',skiprows=1,comments=None)

def not_in(obj):
    rule_list = ['S', 's', 'F', 'f', 'P', 'p']
    for item in rule_list:
        if item in obj:
            return False
    return True

negative = []

for i in range(data.shape[0]):
    if float(data[i,1])<0 and not_in(data[i, 0]):
        negative.append([data[i,0], data[i,1]])

list_out = np.array(negative)



np.savetxt('model_negative.csv',list_out,header='smiles logP',delimiter=',',fmt='%s')



