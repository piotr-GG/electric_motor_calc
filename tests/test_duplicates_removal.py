import unittest
import numpy as np
from utils import Utils
from main import sinfi


class NumpyTest(unittest.TestCase):
    limits = [5, 20, 50]

    def test_duplicate_vrs(self):
        print("TEST_DUPLICATE_VRS()")
        print("*" * 50)
        for limit in self.limits:
            print(f"TEST DLA {limit}")

            with np.load(f"../fixtures/duplikaty_z_vrs, #{limit}.npz") as input:
                rzad_input, sum_input = input.values()

            rzad_processed, sum_processed = Utils.remove_flux_dens_duplicates(rzad_input, sum_input)

            with np.load(f"../fixtures/duplikaty_z_vrs_results, #{limit}.npz") as fixture:
                rzad_fixture, sum_fixture = fixture.values()

            self.assertTrue(np.array_equal(rzad_processed, rzad_fixture))
            self.assertTrue(np.allclose(sum_processed, sum_fixture, rtol=1e-08, atol=1e-10))

        print()

    def test_duplicate_Bfvrs_Blkrp(self):
        print("TEST_DUPLICATE_BFVRS_BLKRP()")
        print("*" * 50)
        for limit in self.limits:
            print(f"TEST DLA {limit}")

            with np.load("../fixtures/sumowanie_Bfvrs_z_Blkrp, #5.npz") as input:
                rzad_input, sum_input = input.values()

            rzad_processed, sum_processed = Utils.remove_flux_dens_duplicates(rzad_input, sum_input)

            with np.load("../fixtures/sumowanie_Bfvrs_z_Blkrp_results, #5.npz") as fixture:
                rzad_fixture, sum_fixture = fixture.values()

            self.assertTrue(np.array_equal(rzad_processed, rzad_fixture))
            self.assertTrue(np.allclose(sum_processed, sum_fixture, rtol=1e-08, atol=1e-10))

        print()

    def test_duplicate_Bfvp(self):
        print("TEST_DUPLICATE_BFVP()")
        print("*" * 50)
        for limit in self.limits:
            print(f"TEST DLA {limit}")

            with np.load(f"../fixtures/sumowanie_z_Bfvp, #{limit}.npz") as input:
                rzad_input, sum_input = input.values()

            rzad_processed, sum_processed = Utils.remove_flux_dens_duplicates_sqrt(rzad_input, sum_input)

            with np.load(f"../fixtures/sumowanie_z_Bfvp_results, #{limit}.npz") as fixture:
                rzad_fixture, sum_fixture = fixture.values()

            self.assertTrue(np.array_equal(rzad_processed, rzad_fixture))
            self.assertTrue(np.allclose(sum_processed, sum_fixture, rtol=1e-08, atol=1e-10))

        print()

    def test_duplicate_Blrs(self):
        print("TEST_DUPLICATE_BLRS()")
        print("*" * 50)
        for limit in self.limits:
            print(f"TEST DLA {limit}")

            with np.load(f"../fixtures/sumowanie_z_Blrs, #{limit}.npz") as input:
                rzad_input, sum_input = input.values()

            rzad_processed, sum_processed = Utils.remove_flux_dens_duplicates(rzad_input, sum_input)

            with np.load(f"../fixtures/sumowanie_z_Blrs_results, #{limit}.npz") as fixture:
                rzad_fixture, sum_fixture = fixture.values()
        try:
            self.assertTrue(np.array_equal(rzad_processed, rzad_fixture))
            self.assertTrue(np.allclose(sum_processed, sum_fixture, rtol=1e-08, atol=1e-10))
        except AssertionError:
            print("AssertionError w limit = " + str(limit))
            print("Sum_processed = ", sum_processed.size)
            print("Sum_fixture = ", sum_processed.size)
            print(sum(sum_processed - sum_fixture))
            raise

        print()

    def test_duplicate_Bs(self):
        print("TEST_DUPLICATE_BS()")
        print("*" * 50)
        for limit in self.limits:
            print(f"TEST DLA {limit}")

            with np.load(f"../fixtures/duplikaty_sum_Bs, #{limit}.npz") as input:
                rzad_input, sum_input = input.values()

            rzad_processed, sum_processed = Utils.remove_flux_dens_duplicates_sin_fi(rzad_input, sum_input, sinfi)

            with np.load(f"../fixtures/duplikaty_sum_Bs_results, #{limit}.npz") as fixture:
                rzad_fixture, sum_fixture = fixture.values()

            self.assertTrue(np.array_equal(rzad_processed, rzad_fixture))
            self.assertTrue(np.array_equal(sum_processed, sum_fixture))

        print()


if __name__ == "__main__":
    unittest.main()
