import numpy

def sub_cost(a, b):
    if a == b:
        return 0
    else:
        return 2

def min_edit_distance(source: str, target: str) -> int:
    '''f
    unction for calculating the min_edit distance between two strings
    Values for deletion insertion and substitution (1, 1 and 2/0) 
    is hardcoded in this function

    takes in two strings 

    returns an integer
    '''

    n = len(source)
    m = len(target)
    # distance matrix
    D = numpy.zeros((n + 1, m + 1))

    for i in range(1, n):
        # deletion cost
        D[i, 0] = D[i - 1, 0] + 1
    for j in range(1, m):
        # insertion cost
        D[0, j] = D[0, j-1] + 1

    print(D)

    # recurrence relation
    for i in range(1, n):
        for j in range(1, m):

            D[i, j] = min(
                D[i-1, j] + 1,
                D[i-1, j-1] + sub_cost(source[i], target[j]),
                D[i, j-1] + 1,
            )

    print(D)

    return D[n, m]


    


def main():
    distance = min_edit_distance("yeah", "yeahbo")
    print(distance)

if __name__ == "__main__":
    main()