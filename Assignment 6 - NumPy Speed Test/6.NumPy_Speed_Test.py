# Assignment: NumPy Speed Test
# Date: 20/02/2026
# Name: Yashaswi N

import time
import numpy as np

def main():
    print("=== NumPy Speed Test: Python List vs NumPy Array ===\n")
    input("Press Enter to start the test...")  

    N = 1_000_000

  
    py_list = list(range(N))
    start_time = time.time()
    py_list_result = [x + 5 for x in py_list]
    list_time = time.time() - start_time
    print(f"Time taken for Python list operation: {list_time:.5f} seconds")

    np_array = np.arange(N)
    start_time = time.time()
    np_array_result = np_array + 5
    numpy_time = time.time() - start_time
    print(f"Time taken for NumPy array operation: {numpy_time:.5f} seconds\n")

    print("=== Observations ===")
    print("1. NumPy arrays are significantly faster than Python lists for large-scale numeric operations.")
    print("2. NumPy uses vectorized operations, which avoids explicit Python loops, improving speed.")
    print("3. Python lists take more memory and processing time due to Python object overhead.\n")

    input("Press Enter to exit...")  

if __name__ == "__main__":
    main()