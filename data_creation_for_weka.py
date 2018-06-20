#data creation for WEKA from second_forsk.txt

filein = open('/home/barvin04/Desktop/second_forsk.txt', 'r')
fileh = filein.readlines()

fileout = open('/home/barvin04/Desktop/dataset_for_weka.csv', 'w') #write
wrt = 'Gx,Gy,Gz,Ay,Az,TYPE'
fileout.write(wrt)
for line in fileh:
    line=line.strip('\n')
    arr = line.split(',')
    #print (arr[9])
    for a in range(3,10):
        if(a<9 and a!=6):
            num = int(arr[a])
            num = str(num)+", "
            fileout.write(num)
        elif(a==9):
            fileout.write(arr[a])
    fileout.write('\n')
    #print (arr[9],'adf') 
    
filein.close()
fileout.close()
