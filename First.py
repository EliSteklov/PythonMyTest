
def count_letters( str ):
    if str == '':
        return 0
    else:
        num = count_letters( str[1:] )
    num = num + 1
    return num

 a = count_letters( "sad fdg dfg dfg dsfg dsfg dfhg fjh ghjgfh   " )




