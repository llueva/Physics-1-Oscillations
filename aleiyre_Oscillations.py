from vpython import *
#Web VPython 3.2
from vpython import *

damping_constant = 0.2 #add this to the top with the other constant values in the code

force = -spring_constant * (position - initial_length) - damping_constant * velocity #just change the force calculation to this instead
