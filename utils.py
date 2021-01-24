import numpy as np

class Utils:
    # TODO: ADD ERROR CHECKING
    @classmethod
    def print_to_file(cls, *array, filename: str, precision: str = "%.3e", separator: str = ",") -> None:
        array_size = [x[0].size for x in array][0]
        for item in array:
            print("tuple: ", item)
            for array_item in item:
                print("array: ", array_item)
                if array_item.size != array_size:
                    print("BŁĄD: ", array_item.size, array_size)
                    raise ValueError("DIFFERENT ARRAY SIZES")
        np.savetxt(filename, *array, delimiter=separator, fmt=precision)

    # TODO: GENERALIZE FUNCTION
    @classmethod
    def remove_flux_dens_duplicates(cls, order, flux_dens):
        i = 0
        while i < order.size:
            indices = np.where(order[i] == order)[0]
            idx_to_del = indices[1:]
            flux_dens[i] = np.sum(flux_dens[indices])
            order = np.delete(order, idx_to_del)
            flux_dens = np.delete(flux_dens, idx_to_del)
            i += 1

        return order, flux_dens

    @classmethod
    def remove_flux_dens_duplicates_sin_fi(cls, order, flux_dens, sinfi = 1.0):
        i = 0
        while i < order.size:
            indices = np.where(order[i] == order)[0]
            idx_to_del = indices[1:]

            if indices.size == 2:
                f_d1, f_d2 = flux_dens[indices]
                flux_dens[i] = np.sqrt(f_d1 ** 2 + f_d2 ** 2 + 2 * f_d1 * f_d2 * sinfi)
            elif indices.size > 2:
                print(order[indices])
                raise Exception("More values than expected")
            order = np.delete(order, idx_to_del)
            flux_dens = np.delete(flux_dens, idx_to_del)
            i += 1

        return order, flux_dens

    @classmethod
    def remove_flux_dens_duplicates_sqrt(cls, order, flux_dens):
        i = 0
        while i < order.size:
            indices = np.where(order[i] == order)[0]
            idx_to_del = indices[1:]

            if indices.size == 2:
                f_d1, f_d2 = flux_dens[indices]
                flux_dens[i] = np.sqrt(f_d1 ** 2 + f_d2 ** 2)
            elif indices.size > 2:
                print(order[indices])
                raise Exception("More values than expected")

            order = np.delete(order, idx_to_del)
            flux_dens = np.delete(flux_dens, idx_to_del)
            i += 1

        return order, flux_dens



    @classmethod
    def remove_flux_dens_duplicates_old(cls, order, flux_dens):
        i = 0
        while i < order.size:
            indices = np.where(order[i] == order)[0]
            idx_to_del = indices[1:]
            if indices.size == 2:
                Bs1, Bs2 = flux_dens[i], flux_dens[idx_to_del[0]]
                flux_dens[i] = np.sqrt(Bs1 ** 2 + Bs2 ** 2 + 2 * Bs1 * Bs2 * sinfi)
            else:
                for j in idx_to_del:
                    flux_dens[i] = flux_dens[i] + flux_dens[j]
            order = np.delete(order, idx_to_del)
            flux_dens = np.delete(flux_dens, idx_to_del)
            i += 1

            return order, flux_dens

    # @classmethod
    # def save_arrays(cls, *args, **kwds, save_to_file):
    #     if save_to_file:
    #         np.savez(*args, **)

    __doc__: str = "" \
                   "This class is intended to serve as an utility class container for general script"
