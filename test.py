
import pandas as pd
import numpy as np
from integration import *



def gen_x2(debut, fin, nb_value):
    """TODO: Docstring for gen_x2.

    :debut: TODO
    :fin: TODO
    :nb_value: TODO
    :returns: TODO

    """
    x_2 = []
    pas = 1/nb_value
    for i in range((fin-debut)*nb_value):
        x = ((i*pas)+debut)
        x_2.append(x*x)

    return x_2



x_2 = gen_x2(-10, 10,1000)
res_int = []

for i in range(1000-1):
    res_int.append(integration_simpson(i,i+1,x_2, 1/1000, 20))

res_int = np.array(res_int)
np.savetxt("int_x2.csv", res_int, delimiter=",")


