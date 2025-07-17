Web VPython 3.2

from vpython import *

scene.background = color.white

spring_constant=1
initial_length=1
mass=1
initial_position=2
initial_velocity=0
dt=0.01
total_time=20
time=0
position= initial_position
velocity= initial_velocity

ball=sphere(
    pos=vector(0, initial_position, 0),
    radius=0.1,
    color=color.blue
    )
    
spring= helix(
    pos=vector(0,0,0),
    axis=ball.pos,
    radius= 0.05,
    coils= 15

    )

graph1= graph(
    title= "position, velocity, acceleration vs. time",
    xtitle= "time in seconds",
    ytitle="position, velocity, acceleration",
    width= 600,
    height= 300  
    )
position_curve= gcurve(
    graph=graph1,
    color=color.magenta,
    label= "position"
    )
velocity_curve= gcurve(
    graph=graph1,
    color=color.cyan,
    label= "velocity"
    )
acceleration_curve= gcurve(
    graph=graph1,
    color=color.blue,
    label= "acceleration"
    )
graph2= graph(
    title= "energy vs. time",
    xtitle= "time in seconds",
    ytitle= "energy in joules",
    width= 600,
    height= 300
    )
kineticenergy_curve= gcurve(
    graph=graph2,
    color=color.orange,
    label= "kinetic energy"
    )
potentialenergy_curve= gcurve(
    graph=graph2,
    color=color.red,
    label= "potential energy"
    )
totalenergy_curve= gcurve(
    graph=graph2,
    color=color.green,
    label= "total energy"
    )


while time < total_time:
    rate(200)
    
    force= -spring_constant*(position - initial_length)
    acceleration= force/mass
    
    velocity = velocity + acceleration*dt
    position= position + velocity*dt
    
    ball.pos.y= position
    spring.axis = ball.pos
    
    kinetic_energy=0.5*mass*velocity**2
    potential_energy=0.5*spring_constant*(position- initial_length)**2
    total_energy=kinetic_energy + potential_energy
    
    position_curve.plot(time, position)
    velocity_curve.plot(time, velocity)
    acceleration_curve.plot(time, acceleration)
    kineticenergy_curve.plot(time, kinetic_energy)
    potentialenergy_curve.plot(time, potential_energy)
    totalenergy_curve.plot(time, total_energy)
    
    time= time + dt
