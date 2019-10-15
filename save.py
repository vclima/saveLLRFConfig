import epics as ep
import csv
import numpy as np

val=np.zeros((338,1))
name=[]
with open('var.csv') as csvfile:
    csvfile=csv.reader(csvfile,delimiter=',',quotechar='"')
    line_count=0
    for row in csvfile:
        if(row[0][0]=='#'):
            name.append(row[0])
            line_count+=1
        else:
            print('Saving '+row[0])
            name.append(row[0])
            val[line_count]=ep.caget(row[0])
            line_count+=1
name=np.array(name)
records = np.rec.fromarrays((name, val[:,0]), names=('keys', 'data'))
with open('var.csv',mode='w') as csvfile:
    writer=csv.writer(csvfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    for i in range(0,records.shape[0]):
            writer.writerow(records[i])
