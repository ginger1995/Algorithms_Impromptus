#!/usr/bin/python
'''
factor_combinations solved in a iterative way.
'''
def getFactors(n):
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i ** 2 <= n:
            if n % i == 0:
                combis.append(combi + [i, n/i])
                todo += [(n/i, i, combi+[i])]
            i += 1
    print combis
    return combis
    
getFactors(48)