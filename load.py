import epics as ep
import csv

with open('var.csv') as csvfile:
    csvfile=csv.reader(csvfile,delimiter=',',quotechar='"')
    line_count=0
    for row in csvfile:
        if(row[0][0]=='#'):
            line_count+=1
        else:
            print('Loading '+row[0])
            ep.caput(row[0],float(row[1]))
