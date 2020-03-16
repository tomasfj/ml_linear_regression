#import tensorflow as tf
import tensorflow as tf
#tf.disable_v2_behavior()
import csv
import numpy as np
import matplotlib.pyplot as plt
from random import uniform


# read data
filename_r_train = 'normal_train_data.csv'
filename_r_test = 'normal_test_data.csv'
filename_r_val = 'normal_val_data.csv'

x_train = []
y_train = []
x_test = []
y_test = []
x_val = []
y_val = []

with open( filename_r_train ) as csv_file:
    csv_reader = csv.reader( csv_file, delimiter = ',' )

    for row in csv_reader:
        x_train.append( [  np.float32(row[1]), np.float32(row[2]), np.float32(row[3]), np.float32(row[4]), np.float32(row[5]), np.float32(row[6]), np.float32(row[7]), np.float32(row[8]), np.float32(1.0) ] )
        y_train.append( np.float32(row[0]) )

with open( filename_r_test ) as csv_file:
    csv_reader = csv.reader( csv_file, delimiter = ',' )

    for row in csv_reader:
        x_test.append( [  np.float32(row[1]), np.float32(row[2]), np.float32(row[3]), np.float32(row[4]), np.float32(row[5]), np.float32(row[6]), np.float32(row[7]), np.float32(row[8]), np.float32(1.0) ] )
        y_test.append( np.float32(row[0]) )

with open( filename_r_val ) as csv_file:
    csv_reader = csv.reader( csv_file, delimiter = ',' )

    for row in csv_reader:
        x_val.append( [  np.float32(row[1]), np.float32(row[2]), np.float32(row[3]), np.float32(row[4]), np.float32(row[5]), np.float32(row[6]), np.float32(row[7]), np.float32(row[8]), np.float32(1.0) ] )
        y_val.append( np.float32(row[0]) )

print( 'DONE READING FILES' )



'''
def J(X, y, theta):
    preds = np.squeeze(np.matmul(X, theta))
    temp =  preds - np.squeeze(y)
    return np.sqrt(np.sum(np.matmul(np.transpose(temp), temp)))
'''

def f2(thetas, x):
    return( thetas[0] * (x[0]) + thetas[1] * (x[1]) + thetas[2] * (x[2]) + thetas[3] * (x[3]) + thetas[4] * (x[4]) + thetas[5] * (x[5]) + thetas[6] * (x[6]) + thetas[7] * x[7] + thetas[8] )

def f3(thetas, x):
    return( thetas[0][0] * (x[0] * 2 ) + thetas[1][0] * (x[1] * 2 ) + thetas[2][0] * (x[2] * 2 ) + thetas[3][0] * (x[3] * 2 ) + thetas[4][0] * (x[4] * 2 ) + thetas[5][0] * (x[5] * 2 ) + thetas[6][0] * (x[6] * 2 ) + thetas[7][0] * x[7] * 2  + thetas[8][0] )


def J(x_test, y_test, thetas):
    sum_e = 0
    for i in range( len(x_test) ):
        #e = ( f( thetas, x_test[i] ) - y_test[i] ) ** 2
        e = ( f3( thetas, x_test[i] ) - y_test[i] ) ** 2
        sum_e += e
    
    return( sum_e / len( x_test ) )



learning_rate = 0.001
tot_iterations = 100

sess = tf.Session()

# Graph Definition

x_data = tf.placeholder(shape=[None, 9], dtype=tf.float32)
y_target = tf.placeholder(shape=[None], dtype=tf.float32)
weight_0 = tf.Variable(tf.random.uniform(shape=[1, 1], minval=-10., maxval=10.0))
weight_1 = tf.Variable(tf.random.uniform(shape=[1, 1], minval=-10., maxval=10.0))
weight_2 = tf.Variable(tf.random.uniform(shape=[1, 1], minval=-10., maxval=10.0))
weight_3 = tf.Variable(tf.random.uniform(shape=[1, 1], minval=-10., maxval=10.0))
weight_4 = tf.Variable(tf.random.uniform(shape=[1, 1], minval=-10., maxval=10.0))
weight_5 = tf.Variable(tf.random.uniform(shape=[1, 1], minval=-10., maxval=10.0))
weight_6 = tf.Variable(tf.random.uniform(shape=[1, 1], minval=-10., maxval=10.0))
weight_7 = tf.Variable(tf.random.uniform(shape=[1, 1], minval=-10., maxval=10.0))
weight_8 = tf.Variable(tf.random.uniform(shape=[1, 1], minval=-10., maxval=10.0))
weights = tf.concat([weight_0, weight_1, weight_2, weight_3, weight_4, weight_5, weight_6, weight_7, weight_8], 0)

# Define the Model
with tf.variable_scope('model_definition') as scope:
    model_output = tf.matmul(x_data, weights)
    scope.reuse_variables()


def loss_l2(predict, gt):
    predict = tf.squeeze(predict)
    #predict = tf.Print(predict,["predict: ", tf.shape(predict)])
    resid = predict - gt
    ret = tf.sqrt(tf.reduce_sum(tf.pow(resid, tf.constant(2.))))
    return ret

loss = loss_l2(model_output, y_target)
my_opt = tf.train.GradientDescentOptimizer(learning_rate)
train_step = my_opt.minimize(loss)

# Graph execution

init = tf.global_variables_initializer()
sess.run(init)


last_loss = 0.0

for i in range(tot_iterations):
    print('Iter: ' + str(i))
    sess.run(train_step, feed_dict={x_data: x_train, y_target: y_train})
    
    theta_tf = sess.run(weights)
    cur_loss = J(x_val,y_val, theta_tf)
    
    if i == 0:
        last_loss = cur_loss
    else:
        if last_loss < cur_loss:
            break
        else:
            last_loss = cur_loss

theta_tf = sess.run(weights)
cur_loss = J(x_test,y_test, theta_tf)

print(cur_loss)
print(theta_tf)
#print('Solution (Tensor flow): J={:.1f}, Theta=({:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f})'.format(cur_loss, theta_tf[0][0], theta_tf[1][0], theta_tf[2][0], theta_tf[3][0], theta_tf[4][0], theta_tf[5][0], theta_tf[6][0], theta_tf[7][0]))
