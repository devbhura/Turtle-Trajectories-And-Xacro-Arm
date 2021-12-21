"""
Calculate the trajectory velocity at each time step
"""

import sympy as sym

from sympy import Function, symbols, Matrix, Eq
from sympy import sin, cos, pi, atan, sqrt, lambdify
from sympy.abc import t


def math_calc(W,H,T, time):
    """
    The function takes in the widht, height, period and time to calculate the linear velocity and angular velocity for the trajectory

    Args:
        W (float): Width of the figure 8 trajectory
        H (float): Height of the figure 8 trajectory
        T (float): Time period of the figure 8 trajectory
        t (float): the time for which to compute the values
    
    Returns:
        v (float): linear velocity for the turtle
        omega (float): angular velocity for the turtle
        theta (float): the angle of the turtle 
        x (float): the x position of the turtle
        y (float): the y position of the turtle
        xdot (float): the x velocity of the turtle
        ydot (float): the y velocity of the turtle
        xddot (float): the x acceleration of the turtle
        yddot (float): the y acceleration of the turtle

    """

    t = symbols('t')

    x = (W/2)*sin(2*pi*t/T)
    y = (H/2)*sin(4*pi*t/T)  

    xdot = x.diff(t)
    xddot = xdot.diff(t)
    ydot = y.diff(t)
    yddot = ydot.diff(t)

    
    v = sqrt(xdot**2 + ydot**2)
    theta = atan(ydot/xdot)
    omega = theta.diff(t)
    
    func1 = lambdify([(t)],v)
    func2 = lambdify([(t)],omega)
    func3 = lambdify([(t)],theta)
    v = func1((time))
    omega = func2((time))
    theta = func3((time))
    funcx = lambdify([(t)],x)
    x = funcx((time))
    funcy = lambdify([(t)],y)
    y = funcy((time))
    funcxdot = lambdify([(t)],xdot)
    xdot = funcxdot((time))
    funcxddot = lambdify([(t)],xddot)
    xddot = funcxddot((time))
    funcydot = lambdify([(t)],ydot)
    ydot = funcydot((time))
    funcyddot = lambdify([(t)],yddot)
    yddot = funcyddot((time))
    
    return v,omega,theta,x,xdot,xddot,y,ydot,yddot


    

    




