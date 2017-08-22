# -*- coding: utf-8 -*-
## - Tervezzünk egy olyan programot, amely milliméterben beolvasott távolságot átalakítja m, cm és mm-re!
print("Üdv, kérlek add meg az átváltandó hosszt, mm-ben!")
raw=float(input())
in_cm=raw/10
in_m=raw/100
print(str(raw) + " mm az átvaltandó érték.")
print("Az " + str(in_cm) + " cm-ben," " valamint " + str(in_m) + " m-ben.")
