import pygame, sys, os
#Just a bunch of shit to figure out how things work in python and pygame

#ARPEL is a fucking liar and this works fine:
pygame.init()
#Displaying Text:
dbfont = pygame.font.Font(pygame.font.get_default_font(),20)
dbtext = "blablabla"
text_surface = dbfont.render(dbtext,True,(0,0,0),(255,255,255))
#Text goes to Rect like literally everything else
textRect = text_surface.get_rect()

#How arrays will work
golist = []
print(len(golist))
golist.append([1,"one"])
golist.append([2,"two"])

print (len(golist))
print(golist[1][1])


