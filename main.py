#!/bin/python
import numpy as np
import plotter as pltr

xbnd = (-1, 1)
ybnd = (-1, 1)
N = 1000

def foo(x, y):
    return x**2+y**2


n = int(np.sqrt(N))
xarg = np.linspace(xbnd[0], xbnd[1], n)
yarg = np.linspace(ybnd[0], ybnd[1], n)

pltr.draw3D(xarg, yarg, foo)
