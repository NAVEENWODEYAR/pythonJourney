import numpy as np

print("=" * 50)
print("NUMPY DATA TYPES DEMO")
print("=" * 50)

# ------------------------------------
# 1. Integer Array
# ------------------------------------
arr_int = np.array([10, 20, 30])

print("\nInteger Array:")
print(arr_int)
print("Data Type:", arr_int.dtype)

# ------------------------------------
# 2. Float Array
# ------------------------------------
arr_float = np.array([1.5, 2.5, 3.5])

print("\nFloat Array:")
print(arr_float)
print("Data Type:", arr_float.dtype)

# ------------------------------------
# 3. Boolean Array
# ------------------------------------
arr_bool = np.array([True, False, True])

print("\nBoolean Array:")
print(arr_bool)
print("Data Type:", arr_bool.dtype)

# ------------------------------------
# 4. String Array
# ------------------------------------
arr_str = np.array(["Python", "NumPy", "AI"])

print("\nString Array:")
print(arr_str)
print("Data Type:", arr_str.dtype)

# ------------------------------------
# 5. Complex Numbers
# ------------------------------------
arr_complex = np.array([2+3j, 4+5j])

print("\nComplex Array:")
print(arr_complex)
print("Data Type:", arr_complex.dtype)

# ------------------------------------
# 6. Specify Data Type Explicitly
# ------------------------------------
arr = np.array([1, 2, 3], dtype=np.float64)

print("\nExplicitly Set dtype=float64")
print(arr)
print("Data Type:", arr.dtype)

# ------------------------------------
# 7. Convert Data Type (astype)
# ------------------------------------
arr2 = np.array([10.5, 20.8, 30.9])

print("\nOriginal Float Array:")
print(arr2)
print("Data Type:", arr2.dtype)

int_arr = arr2.astype(int)

print("\nConverted to Integer:")
print(int_arr)
print("Data Type:", int_arr.dtype)

# ------------------------------------
# 8. Memory Usage
# itemsize = bytes per element
# ------------------------------------
print("\nMemory Information")
print("Item Size:", arr_int.itemsize, "bytes")
print("Total Bytes:", arr_int.nbytes)

# ------------------------------------
# 9. Different Integer Types
# ------------------------------------
a = np.array([1, 2, 3], dtype=np.int8)
b = np.array([1, 2, 3], dtype=np.int16)
c = np.array([1, 2, 3], dtype=np.int32)

print("\nint8 :", a.dtype)
print("int16:", b.dtype)
print("int32:", c.dtype)

print("\nProgram Completed!")