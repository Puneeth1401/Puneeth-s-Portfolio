import math

torque = int(input("Enter the torgue applied, if torque is unknown enter '0': "))
j = int(input("Enter the polar moment of inertia 'J', if 'J' is unknown enter '0': "))
tow = int(input("Enter the shear stress of the body, if shear stress is unknown enter '0': "))
answer1 = input("is the shaft hollow? if yes enter 'yes' else enter 'no': ")

if answer1.lower() == "yes":
    dia_outer = int(input("enter the outer diameter: "))
    dia_inner = int(input("enter the inner diameter: "))
else:
    dia = int(input("enter the diameter: "))

radius = dia / 2

g = int(input("enter the shear modulus of the body, if 'G' is unknown enter '0': "))
theta = int(input("enter theta, if theta is unknown enter '0': "))
length = int(input("enter the length of the shaft, if length is unknown enter '0': "))

if j == 0:
    j = (math.pi / 2) * (radius ** 4)

if torque == 0:
    torque = (g * theta * j) / length
    print(torque)
elif tow != 0:
    torque = tow * j / radius
    print(torque)
elif torque != 0:
    tow = torque * radius / j
    print(tow)
elif theta == 0:
    theta = (tow * length) / (g * radius)
    print(theta)
else:
    print("invalid input")