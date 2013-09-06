from os import listdir
from shutil import move

for zalakatonto in listdir('.'):
    to = zalakatonto.replace('_thumbnail','')
    move(zalakatonto, to)


    
