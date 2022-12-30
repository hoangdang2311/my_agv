#!usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

plt.style.use('fivethirtyeight')

x_vals = []

y_vals = []

x_ref = 0
y_ref = 0
x = 0
y = 0


index = count()

def animate(i):
    plt.cla()
    
    plt.suptitle("Oscillation graph of X_ref and Y_ref")
    
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    
    plt.subplot(2, 1, 1)
    plt.plot(x_vals, y_vals, linewidth=1, color='green')
    plt.ylabel('x_ref')

    #===============================================================

    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    
    plt.subplot(2, 1, 2)
    plt.plot(x_vals, y_vals, linewidth=1, color='blue')
    plt.ylabel('y_ref')

# ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

# plt.tight_layout()

# plt.show()

def subvel_callback(msg: Twist):
    rospy.loginfo("(" + str(msg.linear.x) + ", " + str(msg.angular.z) + ")")
    

    x_ref = msg.linear.x

    y_ref = msg.angular.z

def velsub_callback(vel_data: Twist):
    rospy.loginfo("(" + str(vel_data.linear.x) + ", " + str(vel_data.angular.z) + ")")

    x = vel_data.linear.x
    
    y = vel_data.angular.z

if __name__ == '__main__':
    rospy.init_node("velocity_subscriber")

    sub = rospy.Subscriber("cmd_vel", Twist, callback=subvel_callback)

    vel_sub = rospy.Subscriber("vel_pub", Twist, callback=velsub_callback)

    # rospy.loginfo("(" + str(x_ref) + ", " + str(y_ref) + ")" + ";" + "(" + str(x) + ", " + str(y) +")")

    # rospy.loginfo("Node has been started")


    # ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

    time.sleep(1)

    plt.show()
    
    rospy.spin()