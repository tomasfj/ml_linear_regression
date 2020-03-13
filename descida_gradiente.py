import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


'''
thetas from closed-form
[[ 5.17861557e-01]
 [ 1.02536301e+00]
 [-6.59340438e-01]
 [ 1.00834768e-03]
 [ 1.72917796e+00]
 [-3.21737733e-01]
 [-1.69724067e-01]
 [-1.68532402e-01]
 [-1.25335739e+00]]
'''


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
        x_train.append( [  np.float64(row[1]), np.float64(row[2]), np.float64(row[3]), np.float64(row[4]), np.float64(row[5]), np.float64(row[6]), np.float64(row[7]), np.float64(row[8]) ] )
        y_train.append( np.float64(row[0]) )

with open( filename_r_test ) as csv_file:
    csv_reader = csv.reader( csv_file, delimiter = ',' )

    for row in csv_reader:
        x_test.append( [  np.float64(row[1]), np.float64(row[2]), np.float64(row[3]), np.float64(row[4]), np.float64(row[5]), np.float64(row[6]), np.float64(row[7]), np.float64(row[8]) ] )
        y_test.append( np.float64(row[0]) )

with open( filename_r_val ) as csv_file:
    csv_reader = csv.reader( csv_file, delimiter = ',' )

    for row in csv_reader:
        x_val.append( [  np.float64(row[1]), np.float64(row[2]), np.float64(row[3]), np.float64(row[4]), np.float64(row[5]), np.float64(row[6]), np.float64(row[7]), np.float64(row[8]) ] )
        y_val.append( np.float64(row[0]) )

print( 'DONE READING FILES' )


# gerar 9 thetas random entre -1.000.000 e 1.000.000
thetas = []
for i in range(9):
    thetas.append( ( np.random.random()*20 ) - 10 )

def desenho(erros, epocas):
    plt.plot(epocas, erros)
    plt.savefig('erro_p_epoca_gradiente.png')

def descida(thetas, x, y):
    erros = []

    erro_atual = 0
    erro_anterior = 0
    thetas_anteriores = []

    # nº iterações (n=1000)
    for i in range(10):
        print('Epoca: ' + str(i))
        for n, t in enumerate(thetas):
            thetas[n] = t - ( (0.1) * func_aux(x, y, thetas, n) )
        
        if i == 0:
            erro_atual = erro( thetas, x_val, y_val )
            erro_anterior = erro_atual
            erros.append(erro_atual)
            thetas_anteriores = thetas
        else:
            erro_atual = erro( thetas, x_val, y_val )
            erros.append(erro_atual)
            print( 'erro atual: ' + str(erro_atual) + ' erro anterior: ' + str(erro_anterior) )
            
            if erro_atual > erro_anterior:
                print(i)
                print( thetas )

                desenho(erros, np.arange(i))
                return( thetas_anteriores )
            else:
                erro_anterior = erro_atual
                thetas_anteriores = thetas
    
    desenho(erros, np.arange(10))
    return(thetas)

def f2(thetas, x):
    return( thetas[0] * (x[0]) + thetas[1] * (x[1]) + thetas[2] * (x[2]) + thetas[3] * (x[3]) + thetas[4] * (x[4]) + thetas[5] * (x[5]) + thetas[6] * (x[6]) + thetas[7] * x[7] + thetas[8] )


# recebe um theta (t) e faz a deriava da função f2 (closed-form) em relação a esse theta
def derivada_f2(t, thetas, x, y):
    if t == 8:
        return( 2 * ( f2(thetas, x) - y ) )
    
    return( 2 * ( f2(thetas, x) - y ) * x[t] )


def func_aux(x,y,thetas, j):
    e=0
    for i in range( len(x) ):
        e += derivada_f2(j, thetas, x[i], y[i])

    return( e/len(x) )

def erro(thetas, x_test, y_test):
    sum_e = 0
    for i in range( len(x_test) ):
        #e = ( f( thetas, x_test[i] ) - y_test[i] ) ** 2
        e = ( f2( thetas, x_test[i] ) - y_test[i] ) ** 2
        sum_e += e
    
    return( sum_e / len( x_test ) )

print( 'erro de test: ' + str( erro( descida(thetas, x_train, y_train), x_test, y_test ) ) )