# closed-form

# removed "commentCount" characteristic

import csv
import numpy as np
from numpy.linalg import inv

filename_r_train = 'normal_train_data.csv'
filename_r_test = 'normal_test_data.csv'

x_train = []
y_train = []
x_test = []
y_test = []

# read train data
with open( filename_r_train ) as csv_file:
    csv_reader = csv.reader( csv_file, delimiter = ',' )

    for row in csv_reader:
        x_train.append( [ float(row[0]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]) ] )
        y_train.append( float(row[1]) )

# read test data
with open( filename_r_test ) as csv_file:
    csv_reader = csv.reader( csv_file, delimiter = ',' )

    for row in csv_reader:
        x_test.append( [ float(row[0]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]) ] )
        y_test.append( float(row[1]) )

print( 'DONE READING' )

def closed_form(x, y):
    #print( x.shape() )
    #temp_x = [ [x[i].append(1)] for i in range( len(x) ) ]
    temp_x = []
    for i in x:
        i.append(1.0)
        temp_x.append(i )

    X = np.asarray( temp_x ).reshape( (len( temp_x ), 10) )
    Y = np.asarray( y ).reshape( (len(y),1) )

    return(np.matmul(np.matmul(inv(np.matmul(X.transpose(),X)),X.transpose()),Y))


print( closed_form(x_train, y_train) )