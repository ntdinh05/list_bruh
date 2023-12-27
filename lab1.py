import csv
import matplotlib.pyplot as plt
import math
import numpy as np
frame, rx, ry, rz, tx, ty, tz = [], [], [], [], [], [], []
l = []
with open('data.csv') as file:
    file_read = csv.reader(file)
    for line in file_read:
        l.append(line)

for i in range(5, len(l)):
    frame.append(float(l[i][0]))
    rx.append(float(l[i][2])), ry.append(float(l[i][3])), rz.append(float(l[i][4]))
    tx.append(float(l[i][5])), ty.append(float(l[i][6])), tz.append(float(l[i][7]))

plt.plot(frame, tx)
plt.title('x position over time')
plt.xlabel('Time')
plt.ylabel('x position')
plt.show()

plt.plot(frame, ty)
plt.title('y position over time')
plt.xlabel('Time')
plt.ylabel('y position')
plt.show()

def carPath():
    plt.plot(tx, ty)
    plt.xlabel('x-position')
    plt.ylabel('y-position')
    plt.title('Path travelled by the car')
    plt.show()

carPath()

def carSpeed():
    speed = [0]
    for i in range(1, len(tx)):
        x1, y1 = tx[i - 1], ty[i - 1]
        x2, y2 = tx[i], ty[i]
        s = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
        speed.append(s)
    plt.plot(frame, speed)
    plt.xlabel('Frame')
    plt.ylabel('Speed')
    plt.title("Car's speed for each frame")
    plt.show()

# carSpeed()

def carAcceleration():
    v = [0]
    acceleration = [0]
    for i in range(1, len(tx)):
        x1, y1 = tx[i - 1], ty[i - 1]
        x2, y2 = tx[i], ty[i]
        vxy = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        v.append(vxy)
        acceleration.append(v[len(v) - 1] - v[len(v) - 2])
    print(frame, acceleration)
    plt.plot(frame, acceleration)
    plt.xlabel('Frame')
    plt.ylabel('Acceleration')
    plt.title("Car's acceleration for each frame")
    plt.show()

# carAcceleration()
    
def carHeading():
    angleList = [0]
    for i in range(1, len(tx)):
        x1, y1 = tx[i - 1], ty[i - 1]
        x2, y2 = tx[i], ty[i]
        angle = math.atan2(y2 - y1, x2 - x1) * ( 180 / math.pi)
        angleList.append(angle)
        # print(angleList)
        # print(angle)
    # print(angleList)
    plt.plot(frame, angleList)
    for i in angleList:
        print(i)
    print(angleList)
    plt.xlabel('Frame')
    plt.ylabel('Angle')
    plt.title("Car's heading")
    plt.show()

carHeading()

