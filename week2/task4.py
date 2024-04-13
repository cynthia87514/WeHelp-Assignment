def get_number(index):
    (x,y) = divmod(index,3)
    result = 7*x + 4*y
    print(result)

get_number(1) # print 4 
get_number(5) # print 15 
get_number(10) # print 25 
get_number(30) # print 70