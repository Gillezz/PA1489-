#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit converter
"""
# Asking user for input

print("Hello and welcome to the unit converter!")

height = float(input("Enter current hight in meters over sea, and press enter: "))
speed = float(input("Enter current velocity in km/h, and press enter: "))
temp = float(input("Enter current outside temperature in °C, and press enter:"))

height_feet = round(height * 3.28084, 2)
speed_mph = round(speed * 0.62137, 2) 
temp_f = round(temp * 9 / 5 + 32, 2)

print(f"""
{height} meters over sea is equivalent to {height_feet} feet over sea.
{speed} km/h is equivalent to {speed_mph} 
mph{temp} °C is equivalent to {temp_f} °F""")