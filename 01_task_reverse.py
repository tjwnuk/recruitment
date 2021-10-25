def reverse(N):
    '''
    Reverse function returns reversed number in decimal format.
    If the number is negative, it also returns negative number.
    '''
    if type(N) is not int:
        raise ValueError('You should provide a number of type int')
        # the type of argument passed to a funciton should always be int
    is_negative = False
    if(N<0):  # the function checks sign of the number N to remember it and add after reverse
        is_negative = True
        N = -N
    N_str = str(N) # convert a number to a string
    N_str = N_str[::-1] # reverse the string
    if is_negative:
        N_str = '-' + N_str  # add a sign
    result = int(N_str)  # convert back to an int

    if(result > 2**32):  # check size of the number and return 0 for big numbers
        return 0
    elif(result < -(2**32)-1):
        return 0

    return result

print(reverse(-123456))