

'''
Difference
'''
def diff(seta, setb):
    setc = seta.difference(setb)
    print('DIFF(X-Y): '+str(setc))

def intersection(seta, setb):
    setc = seta.intersection(setb)
    print('DIFF(X and Y): '+str(setc))

def symmetric_difference(seta, setb):
    setc = seta.symmetric_difference(setb)
    print('SYM DIFF: '+str(setc))


if __name__ == "__main__":
    # difference
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}

    print('SET X:'+str(x))
    print('SET X:'+str(y))

    diff(x,y)
    intersection(x,y)
    symmetric_difference(x,y)