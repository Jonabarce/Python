print (" Velkommen til DNBs sparekonto kalkulator")
print (" Din rentesats i prosent er satt til: 2.45 " )
start_beløp = float(input(" Start med å taste inn startbeløp i sparekonto her: "))
print (start_beløp , " er notert ")
spare_tid = float(input(" Vennligst skriv inn ønsket spareperiode oppgitt i antall år "))
print (spare_tid , " er notert ")

g = 1.00 + 0.0245


antall_penger = start_beløp*g**spare_tid

print (" Akkumelert saldo i sparekonto er: " , antall_penger)