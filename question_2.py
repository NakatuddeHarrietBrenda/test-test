#Using a function, create a program that calculates the volume of a cylinder

#approach 1

height = int(input('Enter the height of the cylinder:'))
radius = int(input('Enter the height of the cylinder:'))
volume_of_the_cylinder = 3.14*radius**2*height
print(f'The volume of a cylinder with height{height} and radius{radius} is: {volume_of_the_cylinder}')

#approach 2
import math

height = int(input('Enter the height of the cylinder:'))
radius = int(input('Enter the height of the cylinder:'))
pie_value =math.pi
volume =pie_value * radius**2*height
print(volume)