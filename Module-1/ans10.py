def test (x,y):
    if  x==y or abs(x-y) == 5 or (x+y)==5:
        return True
    else:
        return False


print(test(7,2))   
print(test(8,2))
