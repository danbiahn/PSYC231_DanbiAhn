
def sort_values(i):
    if len(i) == 2:
        if i[0] < i[1]:
            print('keeping the order of two numbers:', i)
        elif i[0] > i[1]:
            i.sort()
            print('changing the order of two numbers:', i)
        else:
            print('two numbers are the same', i) 
    else:
        print ('you need two numbers in this list!')
    

    return i