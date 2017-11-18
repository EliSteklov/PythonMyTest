# String ex3
##################################
# def count_letters( str ):
#     if str == '':
#         return 0
#     else:
#         num = count_letters( str[1:] )
#     num = num + 1
#     return num
#
#  a = count_letters( "sad fdg dfg dfg dsfg dsfg dfhg fjh ghjgfh   " )
##################################

# Ductionary Ex 1
##################################
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
#
# # Version #1
# for key , value  in d1.items():
#     d2[key]=value
#
# # Version #2
# # d2.update(d1)
#
# for key , value  in d2.items():
#        print(key, value)
##################################

# Ductionary Ex 2
##################################
# keys = ['red', 'green', 'blue']
# val = ['#FF0000','#008000', '#0000FF']
# d2={}
# for key in  keys:
#     d2[key]=val.pop()
#   for key , value  in d2.items():
#        print(key, value)
##################################

# Lists Ex 1
##################################
# x = [10, 20, 30]
# y = [40, 50, 60]
#
# y = y + x
# print(y)
##################################

# Lists Ex 2
##################################
# x = [10, 20, 130, 40, 50, 60]
# # # Version #1
# max1 = 0
# for key in x:
#     if (max1 < key):
#         max1 = key
# print (max1)
# # # Version #2
# print(max(x))
##################################

