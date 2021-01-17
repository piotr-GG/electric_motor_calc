from utils import Utils
import numpy as np

if __name__ == "__main__":
    a = np.array([1,2,3,5])
    b = np.array([2,3])
    Utils.print_to_file((a,b), filename = "test1.csv")