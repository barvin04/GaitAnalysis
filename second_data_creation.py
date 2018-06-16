#second in line too
path = '/home/barvin04/Desktop/smaller_dataset/'

acts = ['adl_elderly_jog.txt', 'adl_elderly_stairs.txt', 'adl_elderly_walk.txt', 'fall_elderly_slip.txt', 'fall_elderly_trip.txt']

for name in acts:
    path_name = path+name

    file = open(path_name, 'r')
    filehandle = file.readlines()

    actname= (name.rstrip('.txt')).split('_')[2]
    actname = actname.upper()  #eg: JOG
    
    for lines in filehandle:
        if(lines!='\n'):
            
            lines = lines.strip(";\n'") 
            lines = lines+', ' +actname
            '''
            var = lines.rstrip('\n').rstrip(';') #string
            array_var = var.split(',')[3:9]

            for no in range(len(array_var)): #6
                array_var[no]= int(array_var[no]) #numbers in int type
            
            #print (array_var)
            array_var.append(actname) #TARGET CLASS added !!
            print (array_var)  #list type
            
            #string = ",".join(array_var)#write to output
            #string = string + '\n'
            #print (string) '''
            
            out = open('second_forsk.txt', 'a') #append
            out.write("%s\n"%lines)

            a = filehandle[1]
            out.close()
    file.close()
    
