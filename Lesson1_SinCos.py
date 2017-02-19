import math
import numpy
import matplotlib.pyplot

def sin_cos():
    num_points = 50
    x = numpy.zeros(num_points)
    sin_x = numpy.zeros(num_points)
    cos_x = numpy.zeros(num_points)

    for i in range(num_points):
        x[i] = (2*3.14*i)/49
        sin_x[i] = math.sin(x[i])
        cos_x[i] = math.cos(x[i])
    return x, sin_x, cos_x

x, sin_x, cos_x = sin_cos()

#@show_plot
def plot_me():
    matplotlib.pyplot.plot(x, sin_x)
    matplotlib.pyplot.plot(x, cos_x)
plot_me()
input('Press ENTER to exit')
