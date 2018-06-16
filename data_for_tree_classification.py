#2nd in line 
import os
print (os.getcwd())

path = '/home/barvin04/Desktop/smaller_dataset/'

acts = ['adl_elderly_jog.txt', 'adl_elderly_stairs.txt', 'adl_elderly_walk.txt', 'fall_elderly_slip.txt', 'fall_elderly_trip.txt']
#actn = ['JOG','STAIRS', 'WALK', 'SLIP', 'TRIP']
for name in acts:
    path_name = path+name

    file = open(path_name, 'r')
    filehandle = file.readlines()

    actname= (name.rstrip('.txt')).split('_')[2]
    actname = actname.upper()  #eg: JOG
    
    for lines in filehandle:
        if(lines!='\n'):
            var = lines.rstrip('\n').rstrip(';') #string
            array_var = var.split(',')[3:9]
            #print (array_var)
            array_var.append(actname) #TARGET CLASS added !!
            print (array_var)  #list type
            
            '''string = ",".join(array_var)#write to output
            string = string + '\n'
            print (string)'''
            
            out = open('forsk.txt', 'a') #append
            out.write("%s\n"%array_var)

            out.close()
    file.close()
    
