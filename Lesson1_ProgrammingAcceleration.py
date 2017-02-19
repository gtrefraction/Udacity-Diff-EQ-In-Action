import numpy
import math

earth_mass = 5.97e24 # kg
moon_mass = 7.35e22 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

mp = numpy.array([4,3])
sp = numpy.array([-2.3])

def acceleration(moon_position, spaceship_position):
    vector_moon = moon_position - spaceship_position
    vector_earth = -spaceship_position
    a = gravitational_constant *  (earth_mass/numpy.linalg.norm(vector_earth)**3 * vector_earth + moon_mass/numpy.linalg.norm(vector_moon)**3 * vector_moon)
    return a

a = acceleration(mp,sp)
print(a)
