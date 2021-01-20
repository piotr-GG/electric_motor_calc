import numpy as np


class NumpyUtils:

    @classmethod
    def save_arrays(cls, filename, *args, **kwds):
         np.savez(filename, *args, **kwds)


if __name__ == "__main__":
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    b = np.array([3, 2, 1, 3, 4, 5, 6, 7, 2])
    c = np.array([-34, 23, 66.54, 1e3])

    # NumpyUtils.save_arrays("test_arrays", a, b, c )
    np.savez("test_arrays", a=a, b=b, c=c)

    npzfile = np.load("test_arrays.npz")
    x,y,z = npzfile.values()

    print(np.array_equal(x, a))
    print(np.array_equal(y, b))
    print(np.array_equal(z, c))
    print(np.array_equal(x, b))
