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

key= ['F01_SA']  #add file-keywords here 

array = []
for elem in dirs:    #len(dirs) = 4511
    if(elem[0:6] in key): 
        print (elem)
        array.append(elem)


#dirs <== interested file names-starting
''' if first example of walking it is everything starting with D01 or D02'''

for elem in array: #elem are file names 
    add = elem
    filename = path + add
    file = open(filename, 'r') #type 'r'
    filehandle = file.readlines()

    out = open('/home/barvin04/Desktop/output.txt', 'w') #type 'a' ?
    
    for lines in filehandle:
        out.write(lines)

    file.close()
    out.close()
