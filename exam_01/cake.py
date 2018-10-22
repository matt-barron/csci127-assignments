def divide(A,B,u):
    '''
    a function that divides b by a multiplied by u
    '''
    result = int(B/A * u)
    if result == 1:
        return result, 'Person'
    else:
        return result, 'People'
print(divide(5,10,1))
print(divide(5,10,.5))
print(divide(1,3,1))