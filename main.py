#!/bin/python
import numpy as np
import plotter as pltr

xbnd = (-1, 1)
ybnd = (-1, 1)
N = 1296

def foo(x):
    return x**x


n = int(np.sqrt(N))
xarg = np.linspace(xbnd[0], xbnd[1], n)
yarg = np.linspace(ybnd[0], ybnd[1], n)

pltr.draw_ampl(xarg, yarg, foo)
#pltr.draw_imag(xarg, yarg, foo)
