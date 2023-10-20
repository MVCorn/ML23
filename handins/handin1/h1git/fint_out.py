import numpy as np

if __name__ == '__main__':
    X = np.ones((3,2))
    X *= 4
    X[:,0] *= 2
    y = np.ones(3,)
    y[1] = 10
    y[2] = 20

    print(X.shape[0])
    print()
    print(X.shape[1])
    print()

    """ print(X)
    print()
    print(y)
    print()
    print(y[:, np.newaxis] * X)
    print()
    print(y[0] * X[0, :])
    print()



    k = np.hstack([X, y[:, np.newaxis]])
    print(k)
    print()

    b = 2
    print("k = ", k)
    print()

    print(k[:, [-1]])
    print()

    print(k[:, [0, -1]])
    print()

    print(k[[b*0, b*1], :])
    print()

    print(k[[b*0, b*1], [-1]])
    print() """
