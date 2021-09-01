import math
pi = 22/7
print (" Hei og velkommen til kalkulatoren ")


omkrets = float(input(" Skriv inn kulens omkrets  her: "))
diameter = omkrets/pi
radius = diameter/2
volum = (4/3)*pi*radius**3

print ("Volumet på kulen er ", volum , "kubikkcentimeter")