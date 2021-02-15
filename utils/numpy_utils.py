import numpy as np

# TODO: PUT ALL THE MODULES INTO SINGLE PACKAGE AND THEN FIX THE MOTOR IMPORT!
from model.motor import Motor
from model.motor_calc import MotorCalc
from model.motor_results import MotorResults


class NumpyUtils:

    @classmethod
    def save_arrays(cls, filename, *args, **kwds):
        vals_to_insert = (data.limit, data.Ps, data.PAl, data.Pss, data.Pp)
        Queries.insert_into_motor_results_table(vals_to_insert)
        id_added = Queries.getLastID(table_name="MotorResults")
        print(id_added)

        losses_pssv, losses_ppv = data.rotor_losses()
        losses_psv, losses_palv = data.stator_losses()

        np.savez(filename, *args, **kwds)

    @classmethod
    def save_results(cls, filename, motor_calc: MotorCalc):
        losses_pssv, losses_ppv = motor_calc.rotor_losses()
        losses_psv, losses_palv = motor_calc.stator_losses()
        losses_array = np.array([[losses_psv], [losses_palv], [losses_pssv], [losses_ppv]])
        np.savetxt('test.out', losses_array)

        # TODO: ADJUST THIS CODE TO MY NEEDS!
        import numpy as np
        a = np.array([1, 2, 3, 4, 5])
        b = np.array([5.4, 2.3, 5.3, 2.4])

        c = np.array([a, b])
        print(c)
        np.savez('test.npz', c=c)
        d = np.load('test.npz', allow_pickle=True)
        print(d["c"])
        print(list(d.keys()))


if __name__ == "__main__":
    # a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # b = np.array([3, 2, 1, 3, 4, 5, 6, 7, 2])
    # c = np.array([-34, 23, 66.54, 1e3])
    #
    # # NumpyUtils.save_arrays("test_arrays", a, b, c )
    # np.savez("test_arrays", a=a, b=b, c=c)
    #
    # npzfile = np.load("test_arrays.npz")
    # x, y, z = npzfile.values()
    #
    # print(x)
    # print(y)
    # print(z)
    # print(np.array_equal(x, a))
    # print(np.array_equal(y, b))
    # print(np.array_equal(z, c))
    # print(np.array_equal(x, b))

    m = Motor()
    m_calc = MotorCalc(m, limit=15)
    m_calc.calculate()
    m_res = MotorResults(m_calc)
    NumpyUtils.save_results('dupa', m_calc)
