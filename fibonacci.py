def fibo(x):
    #declare our vars
    F = [0,1]
    first = F[0]
    second = F[1]
    #traverse as far as we need to build the sequence
    for i in range(x-1):
        #calc next number
        next = first + second
        #set up for the next
        first = second
        second = next
        #add our number to the list
        F.append(next)
    #return the number you asked for
    return F[x]


def fact(x):
    #set initial total
    result = 1
    #find the correct range (+1 since we want to include the high bound)
    for i in range(1,x+1):
        #accumulate products
        result *=i
    return result


#two pytest cases
def test_answer1():
    assert fibo(9) == 34

def test_answer2():
    assert fact(5) == 120
