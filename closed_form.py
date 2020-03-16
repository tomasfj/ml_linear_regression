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
    #np.float64(row[0]),
    for row in csv_reader:
        x_train.append( [  np.float64(row[1]), np.float64(row[2]), np.float64(row[3]), np.float64(row[4]), np.float64(row[5]), np.float64(row[6]), np.float64(row[7]), np.float64(row[8]) ] )
        y_train.append( np.float64(row[0]) )

# read test data
with open( filename_r_test ) as csv_file:
    csv_reader = csv.reader( csv_file, delimiter = ',' )

    for row in csv_reader:
        x_test.append( [ np.float64(row[1]), np.float64(row[2]), np.float64(row[3]), np.float64(row[4]), np.float64(row[5]), np.float64(row[6]), np.float64(row[7]), np.float64(row[8]) ] )
        y_test.append( np.float64(row[0]) )

print( 'DONE READING' )

def closed_form(x, y):
    #print( x.shape() )
    #temp_x = [ [x[i] * 2 .append(1)] for i in range( len(x) ) ]
    temp_x = []
    for i in x:
        i.append(1.0)
        temp_x.append(i )

    X = np.asarray( temp_x ).reshape( (len( temp_x ), 9) )
    Y = np.asarray( y ).reshape( (len(y),1) )

    return(np.matmul(np.matmul(inv(np.matmul(X.transpose(),X)),X.transpose()),Y))


#print( closed_form(x_train, y_train) )
thetas = closed_form(x_train, y_train)
print(thetas)

def f(thetas, x):
    return( thetas[0][0] * (x[0]**8) + thetas[1][0] * (x[1]**7) + thetas[2][0] * (x[2]**6) + thetas[3][0] * (x[3]**5) + thetas[4][0] * (x[4]**4) + thetas[5][0] * (x[5]**3) + thetas[6][0] * (x[6]**2) + thetas[7][0] * x[7] + thetas[8][0] )

def f2(thetas, x):
    return( thetas[0][0] * (x[0]) + thetas[1][0] * (x[1]) + thetas[2][0] * (x[2]) + thetas[3][0] * (x[3]) + thetas[4][0] * (x[4]) + thetas[5][0] * (x[5]) + thetas[6][0] * (x[6]) + thetas[7][0] * (x[7]) + thetas[8][0] )

def f3(thetas, x):
    return( thetas[0][0] * (x[0] * 2 ) + thetas[1][0] * (x[1] * 2 ) + thetas[2][0] * (x[2] * 2 ) + thetas[3][0] * (x[3] * 2 ) + thetas[4][0] * (x[4] * 2 ) + thetas[5][0] * (x[5] * 2 ) + thetas[6][0] * (x[6] * 2 ) + thetas[7][0] * (x[7] * 2)  + thetas[8][0] )

def erro(thetas, x_test, y_test):
    sum_e = 0
    for i in range( len(x_test) ):
        #e = ( f( thetas, x_test[i] ) - y_test[i] ) ** 2
        e = ( f2( thetas, x_test[i] ) - y_test[i] ) ** 2
        sum_e += e
    
    return( sum_e / len( x_test ) )

print( erro(thetas, x_test, y_test) )