'''
Code to generate psd based on SEM Tuning
'''

import numpy as np
import gwinc
from gwinc.struct import Struct

budget = gwinc.load_budget('CE2silica')
freq = np.logspace(1, np.log10(7000), 1000)
ifo = Struct.from_file('ifo_tunning2.yaml')

def PSD(Ls, Ts, ifo=ifo, freq=freq):
    
    ifo['Optics']['SRM']['Transmittance'] = Ts
    ifo['Optics']['SRM']['CavityLength'] = Ls
    
    trace = budget.run(ifo=ifo, freq=freq)
    
    return trace.psd