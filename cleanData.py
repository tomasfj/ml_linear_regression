# 0 - A 
# 1 - B index *
# 2 - C videoID 
# 3 - D commentCount *
# 4 - E dislikeCount *
# 5 - F favouriteCount
# 6 - G likeCount *
# 7 - H viewCount *
# 8 - I Time *
# 9 - J commentCount_diff *
# 10 - K dislikeCount_diff *
# 11 - L favouriteCount_diff
# 12 - M likeCount_diff *
# 13 - N viewCount_diff *

from  datetime import datetime
import time

import csv

filename_read = 'count_observation_upload.csv'
filename_write_train = 'train_data.csv'
filename_write_test = 'test_data.csv'
filename_write_val = 'val_data.csv'

data = []

with open(filename_read) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            temp_list = []

            # temp_list = [0 - horaIndex, 1 - commentCount, 2 - dislikeCount, 3 - likeCount, 4 - viewCount, 5 - time_in_secs, 
            #              6 - commentCount_diff, 7 - dislikeCount_diff, 8 - likeCount_diff, 9 - viewCount_diff]

            horaIndex = row[1]
            temp_list.append( row[1] )

            commentCount = row[3]
            temp_list.append( row[3] )

            dislikeCount = row[4]
            temp_list.append( row[4] )
            
            likeCount = row[6]
            temp_list. append( row[6] )

            viewCount = row[7]
            temp_list.append( row[7] )
            
            s = row[8]
            d = datetime.strptime( s, "%Y-%m-%d %H:%M:%S" )
            time_in_secs = time.mktime( d.timetuple() )
            temp_list.append( time_in_secs )

            commentCount_diff = row[9]
            temp_list.append( row[9] )

            dislikeCount_diff = row[10]
            temp_list.append( row[10] )
            
            likeCount_diff = row[12]
            temp_list.append( row[12] )

            viewCount_diff = row[13]
            temp_list.append( row[13] )

            
            data.append( temp_list )
            line_count += 1
            
            #print(horaIndex, commentCount, dislikeCount, likeCount, viewCount, time_in_secs, commentCount_diff, dislikeCount_diff, likeCount_diff, viewCount_diff)

print('DONE READING')
# slip in: training, test, validation
list_train = []
list_test = []
list_val = []

# temp vars
train_count_comment = 0
train_count_comment_diff = 0
train_count_dislike = 0
train_count_dislike_diff = 0
train_count_like = 0
train_count_like_diff = 0
train_count_view = 0
train_count_view_diff = 0

test_count_comment = 0
test_count_comment_diff = 0
test_count_dislike = 0
test_count_dislike_diff = 0
test_count_like = 0
test_count_like_diff = 0
test_count_view = 0
test_count_view_diff = 0

val_count_comment = 0
val_count_comment_diff = 0
val_count_dislike = 0
val_count_dislike_diff = 0
val_count_like = 0
val_count_like_diff = 0
val_count_view = 0
val_count_view_diff = 0

for i in range(len(data)):
    if( i <= len(data) * 0.8 ):
        list_train.append(data[i])

        if( data[i][1] != '' ):
            train_count_comment += float( data[i][1] )
        if( data[i][6] != '' ):
            train_count_comment_diff += float( data[i][6] )
        if( data[i][2] != '' ):
            train_count_dislike += float( data[i][2] )
        if( data[i][7] != '' ):
            train_count_dislike_diff += float( data[i][7] )
        if( data[i][3] != '' ):
            train_count_like += float( data[i][3] )
        if( data[i][8] != '' ):
            train_count_like_diff += float( data[i][8] )
        if( data[i][4] != '' ):
            train_count_view += float( data[i][4] )
        if( data[i][9] != '' ):
            train_count_view_diff += float( data[i][9] )

    elif( ( i > len(data) * 0.8 ) and ( i <= len(data) * 0.9 ) ):
        list_test.append(data[i])

        if( data[i][1] != '' ):
            test_count_comment += float( data[i][1] )
        if( data[i][6] != '' ):
            test_count_comment_diff += float( data[i][6] )
        if( data[i][2] != '' ):
            test_count_dislike += float( data[i][2] )
        if( data[i][7] != '' ):
            test_count_dislike_diff += float( data[i][7] )
        if( data[i][3] != '' ):
            test_count_like += float( data[i][3] )
        if( data[i][8] != '' ):
            test_count_like_diff += float( data[i][8] )
        if( data[i][4] != '' ):
            test_count_view += float( data[i][4] )
        if( data[i][9] != '' ):
            test_count_view_diff += float( data[i][9] )


    else:
        list_val.append(data[i])

        if( data[i][1] != '' ):
            val_count_comment += float( data[i][1] )
        if( data[i][6] != '' ):
            val_count_comment_diff += float( data[i][6] )
        if( data[i][2] != '' ):
            val_count_dislike += float( data[i][2] )
        if( data[i][7] != '' ):
            val_count_dislike_diff += float( data[i][7] )
        if( data[i][3] != '' ):
            val_count_like += float( data[i][3] )
        if( data[i][8] != '' ):
            val_count_like_diff += float( data[i][8] )
        if( data[i][4] != '' ):
            val_count_view += float( data[i][4] )
        if( data[i][9] != '' ):
            val_count_view_diff += float( data[i][9] )

print( 'DONE SPLITING' )

# write train
with open(filename_write_train, mode = 'a') as new_csv_file:
    csv_writer = csv.writer(new_csv_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

    #csv_writer.writerow([horaIndex, commentCount, dislikeCount, likeCount, viewCount, time_in_secs, commentCount_diff, dislikeCount_diff, likeCount_diff, viewCount_diff])
    
    for i in range(len(list_train)):
        if( list_train[i][1] == '' ): # commentCount
            list_train[i][1] = train_count_comment / len(list_train)
        if( list_train[i][2] == '' ): # dislikeCount
            list_train[i][2] = train_count_dislike / len(list_train)
        if( list_train[i][3] == '' ): # likeCount
            list_train[i][3] = train_count_like / len(list_train)
        if( list_train[i][4] == '' ): # viewCount
            list_train[i][4] = train_count_view / len(list_train)
        if( list_train[i][6] == '' ): # commentCount_diff
            list_train[i][6] = train_count_comment_diff / len(list_train)
        if( list_train[i][7] == '' ): # dislikeCount_diff
            list_train[i][7] = train_count_dislike_diff / len(list_train)
        if( list_train[i][8] == '' ): # likeCount_diff
            list_train[i][8] = train_count_like_diff / len(list_train)
        if( list_train[i][9] == '' ): # viewCount_diff
            list_train[i][9] = train_count_view_diff / len(list_train)
        
        
        csv_writer.writerow(list_train[i])

print( 'DONE WRITING FILE TRAIN' )

# write test
with open(filename_write_test, mode = 'a') as new_csv_file:
    csv_writer = csv.writer(new_csv_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

    #csv_writer.writerow([horaIndex, commentCount, dislikeCount, likeCount, viewCount, time_in_secs, commentCount_diff, dislikeCount_diff, likeCount_diff, viewCount_diff])
    
    for i in range(len(list_test)):
        if( list_test[i][1] == '' ): # commentCount
            list_test[i][1] = test_count_comment / len(list_test)
        if( list_test[i][2] == '' ): # dislikeCount
            list_test[i][2] = test_count_dislike / len(list_test)
        if( list_test[i][3] == '' ): # likeCount
            list_test[i][3] = test_count_like / len(list_test)
        if( list_test[i][4] == '' ): # viewCount
            list_test[i][4] = test_count_view / len(list_test)
        if( list_test[i][6] == '' ): # commentCount_diff
            list_test[i][6] = test_count_comment_diff / len(list_test)
        if( list_test[i][7] == '' ): # dislikeCount_diff
            list_test[i][7] = test_count_dislike_diff / len(list_test)
        if( list_test[i][8] == '' ): # likeCount_diff
            list_test[i][8] = test_count_like_diff / len(list_test)
        if( list_test[i][9] == '' ): # viewCount_diff
            list_test[i][9] = test_count_view_diff / len(list_test)
        
        
        csv_writer.writerow(list_test[i])

print( 'DONE WRITING FILE TEST' )

# write val
with open(filename_write_val, mode = 'a') as new_csv_file:
    csv_writer = csv.writer(new_csv_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

    #csv_writer.writerow([horaIndex, commentCount, dislikeCount, likeCount, viewCount, time_in_secs, commentCount_diff, dislikeCount_diff, likeCount_diff, viewCount_diff])
    
    for i in range(len(list_val)):
        if( list_val[i][1] == '' ): # commentCount
            list_val[i][1] = val_count_comment / len(list_val)
        if( list_val[i][2] == '' ): # dislikeCount
            list_val[i][2] = val_count_dislike / len(list_val)
        if( list_val[i][3] == '' ): # likeCount
            list_val[i][3] = val_count_like / len(list_val)
        if( list_val[i][4] == '' ): # viewCount
            list_val[i][4] = val_count_view / len(list_val)
        if( list_val[i][6] == '' ): # commentCount_diff
            list_val[i][6] = val_count_comment_diff / len(list_val)
        if( list_val[i][7] == '' ): # dislikeCount_diff
            list_val[i][7] = val_count_dislike_diff / len(list_val)
        if( list_val[i][8] == '' ): # likeCount_diff
            list_val[i][8] = val_count_like_diff / len(list_val)
        if( list_val[i][9] == '' ): # viewCount_diff
            list_val[i][9] = val_count_view_diff / len(list_val)
        
        
        csv_writer.writerow(list_val[i])

print( 'DONE WRITING FILE VAL' )

print( 'LIST_TRAIN SIZE: ' + str( len( list_train ) ) )
print( 'LIST_TEST SIZE: ' + str( len( list_test ) ) )
print( 'LIST_VAL SIZE: ' + str( len( list_val ) ) )