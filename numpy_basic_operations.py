"""
NumPy Basic Operations — Beginner Practice
Run: python numpy_basic_operations.py
Install: pip install numpy
"""

import numpy as np


def main():
    print("=" * 50)
    print("NUMPY BASIC OPERATIONS")
    print("=" * 50)

    # 1. Creating arrays
    arr_1d = np.array([1, 2, 3, 4, 5])
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    zeros = np.zeros((2, 3))
    ones = np.ones((2, 2))
    rng = np.arange(0, 10, 2)          # [0 2 4 6 8]
    linspace = np.linspace(0, 1, 5)    # 5 evenly spaced points 0..1

    print("\n1. Creating Arrays")
    print("1D array:", arr_1d)
    print("2D array:\n", arr_2d)
    print("Zeros:\n", zeros)
    print("Ones:\n", ones)
    print("Arange:", rng)
    print("Linspace:", linspace)

    # 2. Array properties
    print("\n2. Array Properties")
    print("Shape of 2D:", arr_2d.shape)
    print("Dimensions:", arr_2d.ndim)
    print("Data type:", arr_1d.dtype)
    print("Total elements:", arr_2d.size)

    # 3. Basic math (element-wise)
    a = np.array([10, 20, 30, 40])
    b = np.array([1, 2, 3, 4])
    print("\n3. Element-wise Math")
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)
    print("a ** 2 =", a ** 2)
    print("sqrt(a) =", np.sqrt(a))

    # 4. Aggregation / statistics
    print("\n4. Aggregation & Statistics")
    print("Sum:", arr_1d.sum())
    print("Mean:", arr_1d.mean())
    print("Median:", np.median(arr_1d))
    print("Min:", arr_1d.min(), "| Max:", arr_1d.max())
    print("Standard deviation:", arr_1d.std())
    print("Column sums of 2D:", arr_2d.sum(axis=0))
    print("Row sums of 2D:", arr_2d.sum(axis=1))

    # 5. Indexing and slicing
    print("\n5. Indexing & Slicing")
    print("First element:", arr_1d[0])
    print("Last element:", arr_1d[-1])
    print("Slice [1:4]:", arr_1d[1:4])
    print("Reverse:", arr_1d[::-1])
    print("2D row 0:", arr_2d[0])
    print("2D element [1,2]:", arr_2d[1, 2])
    print("Boolean mask (arr_1d > 2):", arr_1d[arr_1d > 2])

    # 6. Reshaping
    print("\n6. Reshaping")
    reshaped = np.arange(1, 7).reshape(2, 3)
    print("Reshaped 1..6 to 2x3:\n", reshaped)
    print("Flattened:", reshaped.flatten())
    print("Transpose:\n", reshaped.T)

    # 7. Stacking & concatenation
    print("\n7. Stacking")
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    print("Vertical stack:\n", np.vstack([x, y]))
    print("Horizontal stack:", np.hstack([x, y]))

    # 8. Random numbers
    print("\n8. Random Numbers")
    np.random.seed(42)  # reproducible
    print("Random 1x5 floats:", np.random.rand(5))
    print("Random ints 0-9:", np.random.randint(0, 10, 5))

    # 9. Useful operations
    print("\n9. Useful Operations")
    print("Unique of [1,2,2,3,3,3]:", np.unique([1, 2, 2, 3, 3, 3]))
    print("Sorted descending:", np.sort(arr_1d)[::-1])
    print("Where (arr_1d > 2):", np.where(arr_1d > 2, arr_1d, 0))
    print("Clip to [2,4]:", np.clip(arr_1d, 2, 4))
    print("Dot product [1,2].[3,4]:", np.dot([1, 2], [3, 4]))

    print("\n" + "=" * 50)
    print("Done! Explore by changing values and re-running.")
    print("=" * 50)


if __name__ == "__main__":
    main()
