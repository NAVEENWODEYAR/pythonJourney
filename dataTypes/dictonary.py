# Python dict vs Java HashMap
# ===========================

# Python:
# d = {}
#
# Java:
# Map<String, Integer> map = new HashMap<>();

student = {}

# --------------------------------------------------
# 1. ADD / INSERT
# --------------------------------------------------

student["name"] = "Rahul"
student["age"] = 25

# Java equivalent:
# map.put("name", "Rahul");
# map.put("age", 25);

print("After adding:", student)


# --------------------------------------------------
# 2. ACCESS VALUE
# --------------------------------------------------

print("Name:", student["name"])

# Java equivalent:
# System.out.println(map.get("name"));


# --------------------------------------------------
# 3. UPDATE VALUE
# --------------------------------------------------

student["age"] = 26

# Java equivalent:
# map.put("age", 26);

print("After update:", student)


# --------------------------------------------------
# 4. CHECK IF KEY EXISTS
# --------------------------------------------------

if "name" in student:
    print("name exists")

# Java equivalent:
# if (map.containsKey("name")) {
#     System.out.println("name exists");
# }


# --------------------------------------------------
# 5. GET VALUE SAFELY
# --------------------------------------------------

print(student.get("city"))

# Output:
# None

# Java equivalent:
# map.get("city");
#
# Output:
# null


# --------------------------------------------------
# 6. ACCESS NON-EXISTING KEY
# --------------------------------------------------

# print(student["city"])
#
# Python gives:
# KeyError
#
# Java:
# map.get("city");
#
# Java HashMap gives:
# null


# --------------------------------------------------
# 7. REMOVE
# --------------------------------------------------

del student["age"]

# Java equivalent:
# map.remove("age");

print("After removing age:", student)


# --------------------------------------------------
# 8. ITERATION
# --------------------------------------------------

for key, value in student.items():
    print(key, "=", value)

# Java equivalent:
#
# for (Map.Entry<String, Object> entry : map.entrySet()) {
#     System.out.println(
#         entry.getKey() + " = " + entry.getValue()
#     );
# }


# --------------------------------------------------
# 9. DUPLICATE KEY
# --------------------------------------------------

student["name"] = "Amit"
student["name"] = "John"

print("Duplicate key:", student)

# The old value is replaced.
#
# Java:
# map.put("name", "Amit");
# map.put("name", "John");
#
# Same behavior: "Amit" is replaced by "John"


# --------------------------------------------------
# 10. DIFFERENT DATA TYPES
# --------------------------------------------------

data = {
    "name": "Rahul",      # String
    "age": 25,            # Integer
    "salary": 50000.50,   # Float
    "active": True,       # Boolean
    "skills": ["Java", "Python"]  # List
}

print("Mixed data:", data)


# --------------------------------------------------
# IMPORTANT DIFFERENCES
# --------------------------------------------------

print("""
Python dict vs Java HashMap

1. Python       -> dict
   Java         -> HashMap

2. Add/update:
   Python       -> d[key] = value
   Java         -> map.put(key, value)

3. Get:
   Python       -> d[key]
   Java         -> map.get(key)

4. Check key:
   Python       -> key in d
   Java         -> map.containsKey(key)

5. Remove:
   Python       -> del d[key]
   Java         -> map.remove(key)

6. Missing key:
   Python d[key] -> KeyError
   Java get()    -> null

7. Ordering:
   Python dict   -> preserves insertion order
   Java HashMap  -> order is NOT guaranteed

8. Type system:
   Python dict   -> dynamically typed
   Java HashMap  -> usually uses generics for type safety

9. Both:
   - Store key-value pairs
   - Keys must be hashable
   - Duplicate keys are not allowed
   - Average lookup is O(1)
   - Average insertion is O(1)
""")