#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys



print "\n\nDonner l'année:"
annee=input()

print "\nDonner le mois:"
imois=raw_input()
if imois=="janvier":
    mois=1
if imois=="fevrier":
    mois=2
if imois=="mars":
    mois=3
if imois=="avril":
    mois=4
if imois=="mai":
    mois=5
if imois=="juin":
    mois=6
if imois=="juillet":
    mois=7
if imois=="aout":
    mois=8
if imois=="septembre":
    mois=9
if imois=="octobre":
    mois=10
if imois=="novembre":
    mois=11
if imois=="decembre":
    mois=12
if imois not in ["janvier", "fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]:
    print "Erreur dans la saisie du mois"
    sys.exit()

print "\nDonner le jour:"
jour=input()



if mois == 0 or mois == 2 or mois == 4 or mois == 6 or mois == 9 or mois == 11:
    if jour>30:
        print "Erreur dans la saisie du jour (il n'y a pas autant de jours dans ce mois)"
        sys.exit(0)
if mois == 2:
    if jour>28:
        print "Erreur dans la saisie du jour (il n'y a pas autant de jours dans ce mois)"
        sys.exit(0)
if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
    if jour>31:
        print "Erreur dans la saisie du jour (il n'y a pas autant de jours dans ce mois)"
        sys.exit(0)


journext = jour + 1


if mois == 0 or mois == 2 or mois == 4 or mois == 6 or mois == 9 or mois == 11:
    if journext>31:
        journext=journext%31
        mois = mois +1



if mois == 2:
    if journext>28:
        journext=journext%28
        mois = mois +1


if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10:
    if journext>31:
        journext=journext%31
        mois = mois +1

if mois == 12:
    if journext > 31:
        mois = 1
        journext = 1
        annee = annee + 1



if mois == 1:
    mois="janvier"
if mois == 2:
    mois="février"
if mois == 3 :
    mois="mars"
if mois == 4:
    mois="avril"
if mois == 5:
    mois="mai"
if mois == 6:
    mois="juin"
if mois == 7:
    mois="juillet"
if mois == 8:
    mois="aout"
if mois == 9:
    mois="septembre"
if mois == 10:
    mois="octobre"
if mois == 11:
    mois="novembre"
if mois == 12:
    mois="decembre"

print "\nLe jour suivant est: ",journext, mois, annee
