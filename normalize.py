import csv

# filename_read = 'val_data.csv'
# filename_write = 'normal_val_data.csv'

filename_read = 'test_data.csv'
filename_write = 'normal_test_data.csv'

# filename_read = 'train_data.csv'
# filename_write = 'normal_train_data.csv'

data = []

maxs_mins = [ [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]  ]

# reading from file
with open( filename_read ) as csv_file:
    csv_reader = csv.reader( csv_file, delimiter = ',' )
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            
            for i in range( len(row) ):
                maxs_mins[i][0] = float( row[i] )
                maxs_mins[i][1] = float( row[i] )

            data.append(row)
            line_count += 1

        else:
            for i in range( len(row) ):
                if( float( row[i] ) > maxs_mins[i][0] ):
                    maxs_mins[i][0] = float( row[i] )
                if( float( row[i] ) < maxs_mins[i][1] ):
                    maxs_mins[i][1] = float( row[i] )

            data.append(row)
            line_count += 1

# testing
print('LINECOUNT = ' + str(line_count) + '\n')

for i in range( len(maxs_mins) ):
    print( 'MAX: ' + str(maxs_mins[i][0]) + ' MIN: ' + str(maxs_mins[i][1]) + '\n' )


with open(filename_write, mode = 'a') as csv_file:
    csv_writer = csv.writer( csv_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL )

# writing to file
    for row in data:
        for i in range( len(row) ):
            row[i] = ( float( row[i] ) - maxs_mins[i][1] ) / ( maxs_mins[i][0] - maxs_mins[i][1] )
        
        csv_writer.writerow( row )
