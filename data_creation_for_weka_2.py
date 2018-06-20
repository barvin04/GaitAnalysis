#data creation from the FRESH FALL data by Pragya
#this is one of the last tries, that dataset to work on has 2*(206) data-rows
import random

fileout = open('/home/barvin04/Desktop/dataset_for_weka.csv', 'w') #write
wrt = 'Gx,Gy,Gz,Ay,Az,TYPE\n'
fileout.write(wrt)


for var in range(206):  #results are good only if no. of training cases are equal for both the classes !!!!
    Gx= random.randint(114,122)
    Gy= random.randint(12,16)
    Gz= random.randint(114,122)
    Ax=0
    Ay=random.randint(230,255)
    Az=random.randint(230,255)
    
    idle = str(Gx)+','+str(Gy)+','+str(Gz)+','+str(Ax)+','+str(Ay)+','+str(Az)+','+ 'IDLE\n'
    fileout.write(idle)

filein = open('/home/barvin04/Desktop/myfile.txt', 'r') #read
fileh = filein.readlines()
for dataline in fileh:
    dataline = dataline.strip('\n')
    dataline = dataline + ', FALL\n'
    fileout.write(dataline)
   
filein.close()
fileout.close()
#filein.close()
