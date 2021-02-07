import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    print(ROOT_DIR)
    print("__file__", __file__)
    print("os.path.abspath(__file__)", os.path.abspath(__file__))
    print("os.path.dirname(os.path.abspath(__file__))", os.path.dirname(os.path.abspath(__file__)))