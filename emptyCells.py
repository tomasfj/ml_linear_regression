import csv

filename = 'train_data.csv'

with open(filename) as csv_file:
    csv_reader = csv.reader( csv_file, delimiter = ',' )
    line_count = 0

    for row in csv_reader:
        for cell in row:
            if cell == '':
                print( 'FOUND AN EMPTY CELL AT: ' + str(line_count) )
                print( str( row )  + '\n')

    line_count += 1

print( 'DONE' )