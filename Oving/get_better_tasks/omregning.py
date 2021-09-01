en_tomme = 2.54
en_fot = en_tomme*12
# Definerer tomme og fot

print (" Hei og velkommen ")
cm = float(input(" Vennligst skriv inn ønsket antall centimeter her:"))

antall_tomme = cm/en_tomme

antall_fot = antall_tomme//12
antall_ny_tomme = (round(antall_tomme%12))

print (cm , " centimenter tilsvarer ca ", antall_fot ,"fot og", antall_ny_tomme , "tommer")
