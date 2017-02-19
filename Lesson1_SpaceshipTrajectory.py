# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 21:31:34 2017

@author: willedwa
"""
import math
import numpy
import matplotlib.pyplot

h = 0.01 # s
earth_mass = 5.97e24 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

def acceleration(spaceship_position):
    vector_earth = -spaceship_position
    return gravitational_constant *  earth_mass/numpy.linalg.norm(vector_earth)**3 * vector_earth

def ship_trajectory():
    num_steps = 13000000
    x = numpy.zeros([num_steps + 1, 2]) # m
    v = numpy.zeros([num_steps + 1, 2]) # m / s

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3

    for step in range(num_steps):
        x[step + 1] = x[step] + h * v[step]
        v[step + 1] = v[step] + h * acceleration(x[step]) 

    return x, v

x, v = ship_trajectory()

def plot_me():
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.scatter(0, 0)
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
plot_me()