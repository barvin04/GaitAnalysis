#first in line 
'''
through this all the data for GaitAnalysis can be obtained
i have focues on adl: walk, jog, stairs; and fall: slip, trip
'''
import os
#path : os.getcwd()

#parent_path = '/home/barvin04/Desktop/SmartStickData'
path = "/home/barvin04/Desktop/SmartStickData/"
dirs = os.listdir(path)

key= ['D02_SE']  #taking only elderly, even then dataset is huge 
#key2 ='F05_SE'#'D06_SE'  '''make changes in these two keys for new files'''
#key3 ='F03_SE'

array = []
for elem in dirs:
    if(elem[0:6] in key): #or elem[0:6]==key2): #or elem[0:6]==key3):
        print (elem)
        array.append(elem)

        
#

'''filename = '/home/barvin04/Desktop/SmartStickData/D01_SA01_R01.txt'
file = open(filename, 'r')
fileh= file.readlines()
print (len(fileh))'''

#dirs <== interested file names-starting
''' if first example of walking it is everything starting with D01 or D02'''

for elem in array: #elem are file names 
    add = elem
    filename = path + add
    file = open(filename, 'r') #type 'r'
    filehandle = file.readlines()

    out = open('/home/barvin04/Desktop/output.txt', 'w') #type 'a'
    for lines in filehandle:
        out.write(lines)

    file.close()
    out.close()
