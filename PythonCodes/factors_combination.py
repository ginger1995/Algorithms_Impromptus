#!/usr/bin/python
'''
factor_combinations solved in both recursive and iterative way.
'''


def getFactors_itera(n):
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i ** 2 <= n:
            if n % i == 0:
                combis.append(combi + [i, n / i])
                todo += [(n / i, i, combi + [i])]
            i += 1
    print combis
    return combis


def getFactors_recur(self, arg):
    pass

getFactors_itera(36)
