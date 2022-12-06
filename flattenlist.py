# Burada asagıdaki gibi verilen listeyi duzelterek cıkaracagız.

#input - L = [[[1, 2, 3], [4, 5]], 6]
#output [1, 2, 3, 4, 5, 6] olmali.


def flatten(a):
    flatten=[]
    for e in a:
        if type(e) is list:
            for i in e:
                flatten.append(i)
        else:
            flatten.append(e)
    return flatten

L = [[[1, 2, 3], [4, 5]], 6]
print("The original list: ",L )
print("The new list: ",flatten(flatten(L)))


            