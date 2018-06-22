#data creation from the FRESH FALL data by Pragya
#this is one of the last tries, that dataset to work on has 2*(206) data-rows
import random

fileout = open('/home/barvin04/Desktop/dataset_for_weka.csv', 'w') #write
wrt = 'Gx,Gy,Gz,Ay,Az,TYPE\n'
fileout.write(wrt)


filein1 = open('/home/barvin04/Desktop/IDLE.txt', 'r') #read
fileg = filein1.readlines()
for dataline in fileg:
    dataline = dataline.strip('\n')
    if(len(dataline.split(','))==5):
        dataline = dataline + ',IDLE \n'
        fileout.write(dataline)

filein = open('/home/barvin04/Desktop/FALL.txt', 'r') #read
fileh = filein.readlines()
for dataline in fileh:
    dataline = dataline.strip('\n')
    if(len(dataline.split(','))==5):
        dataline = dataline + ', FALL\n'
        fileout.write(dataline)
       
filein.close()
fileout.close()
#filein.close()
