from utils import Utils
import numpy as np
from numpy_utils import NumpyUtils
if __name__ == "__main__":
    # a = np.array([1,2,3,5])
    # b = np.array([2,3])
    # # Utils.print_to_file((a,b), filename = "test1.csv")
    # # NumpyUtils.save_arrays("fixtures/test", a = a, b = b)
    x, y = np.load("fixtures/duplikaty_sum_Bs, #5.npz").values()
    print(x, y)

    # a = range(1,5)
    # print(map(lambda x: x**2, a))
    # for val in map(lambda x:x**2 , a):
    #     print(val)


    def remove_flux_dens_duplicates(order, flux_dens, func = None):
        i = 0
        while i < order.size:
            indices = np.where(order[i] == order)[0]
            idx_to_del = indices[1:]
            flux_dens[i] = func()
            order = np.delete(order, idx_to_del)
            flux_dens = np.delete(flux_dens, idx_to_del)
            i += 1

        return order, flux_dens