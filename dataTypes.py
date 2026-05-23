# Python Data Types Demonstration

print('session - Python Data Types')
print('====================')
print("=== PYTHON DATA TYPES ===\n")

# 1. Text Type
text_value = "Hello, Python!"
print("Text Type:")
print("Value:", text_value)
print("Data Type:", type(text_value))
print()

# 2. Numeric Types
integer_value = 10
float_value = 10.5
complex_value = 2 + 3j

print("Numeric Types:")
print("Integer:", integer_value, "-", type(integer_value))
print("Float:", float_value, "-", type(float_value))
print("Complex:", complex_value, "-", type(complex_value))
print()

# 3. Sequence Types
list_value = [1, 2, 3, 4]
tuple_value = (10, 20, 30)
range_value = range(5)

print("Sequence Types:")
print("List:", list_value, "-", type(list_value))
print("Tuple:", tuple_value, "-", type(tuple_value))
print("Range:", list(range_value), "-", type(range_value))
print()

# 4. Mapping Type
dict_value = {
    "name": "Alice",
    "age": 25
}

print("Mapping Type:")
print("Dictionary:", dict_value)
print("Data Type:", type(dict_value))
print()

# 5. Set Types
set_value = {1, 2, 3, 4}
frozenset_value = frozenset({5, 6, 7})

print("Set Types:")
print("Set:", set_value, "-", type(set_value))
print("Frozen Set:", frozenset_value, "-", type(frozenset_value))
print()

# 6. Boolean Type
bool_value = True

print("Boolean Type:")
print("Value:", bool_value)
print("Data Type:", type(bool_value))
print()

# 7. Binary Types
bytes_value = b"Hello"
bytearray_value = bytearray(5)
memoryview_value = memoryview(bytes_value)

print("Binary Types:")
print("Bytes:", bytes_value, "-", type(bytes_value))
print("Bytearray:", bytearray_value, "-", type(bytearray_value))
print("Memoryview:", memoryview_value, "-", type(memoryview_value))
print()

# 8. None Type
none_value = None

print("None Type:")
print("Value:", none_value)
print("Data Type:", type(none_value))
print()

print("=== END OF PROGRAM ===")