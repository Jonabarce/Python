import math #importerer så jeg kan bruke math.pi



    



r = float (input (" Hva skal radiusen være?")) # radius for en sirkel
print (r, " Det er notert ")
h = float(input (" Hva skal høyden være?")) #høyde
print (h, ", Det er notert")
d = r*2 #diameter for en sirkel




A_sirkel = math.pi * r**2
omkrets = math.pi*d
A_sylinder = 2*math.pi*r**2 + 2*math.pi*r*h



print (" Ved verdiene:" , r , " som radius og", h , "som høyde får vi følgende svar:")
print("Omkrets av sirkelen:", omkrets)
print("Areal av sirkelen:", A_sirkel)
print("Areal av sylinderen:", A_sylinder)

r1 = round (A_sirkel)
r2 = round (A_sylinder)
r3 = round (omkrets)

num = float(input (" Ønsker du å avrunde svarene? Skriv '1' vis det er ønskelig, og skriv '2' hvis du vil avslutte "))
if num<2:
    print ("Omkrets av sirkelen er ca:" , r3)
    print ("Areal av sirkelen er ca:", r1)
    print ("Areal av sylinderen er ca:", r2)
elif num>1:
    print (" Den er god, da avsluttes kalkulatoren ")
