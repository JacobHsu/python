# -*- coding: utf-8 -*-  

import csv  
f = open('stock.csv', 'r')  
for row in csv.reader(f):  
    print row  
f.close()