#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: ImC:\Users\chris\OneDrive\Documents\Poly\Inf1007\Exercices\2021h-ch6-1-exercices-ChristianRoy15\exercice.pyportez vos modules ici
import sys
sys.path.insert(0, 'C:\\Users\chris\OneDrive\Documents\Poly\Inf1007\Exercices\\2021h-ch6-1-exercices-ChristianRoy15\exercice.py')
from exercice_ch6 import frequence
import math

# TODO: Définissez vos fonction ici
def cpmpute_volume_and_mass(a=5, b=8, c=10, mass_volum=1):
    volume = 4 / 3 * math.pi * a * b * c
    mass = mass_volum * volume
    return volume, mass



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    mass_vol = cpmpute_volume_and_mass()
    print(mass_vol)

    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("test test test test"))




