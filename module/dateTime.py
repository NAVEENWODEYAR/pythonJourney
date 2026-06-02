# ============================================
# Python DateTime Module Demonstration Program
# ============================================

# Import datetime module
import datetime

# ------------------------------------------------
# 1. Display Current Date and Time
# ------------------------------------------------

# datetime.now() returns current local date and time
current_datetime = datetime.datetime.now()

print("1. Current Date and Time")
print(current_datetime)
print()


# ------------------------------------------------
# 2. Get Current Date Only
# ------------------------------------------------

# today() returns current date
current_date = datetime.date.today()

print("2. Current Date")
print(current_date)
print()


# ------------------------------------------------
# 3. Create a Specific Date
# ------------------------------------------------

# Creating a date object
my_date = datetime.date(2025, 12, 25)

print("3. Custom Date")
print(my_date)
print()


# ------------------------------------------------
# 4. Create a Specific Time
# ------------------------------------------------

# Creating a time object
my_time = datetime.time(10, 30, 45)

print("4. Custom Time")
print(my_time)
print()


# ------------------------------------------------
# 5. Create a Custom DateTime Object
# ------------------------------------------------

custom_datetime = datetime.datetime(
    2025,   # Year
    6,      # Month
    15,     # Day
    14,     # Hour
    30,     # Minute
    20      # Second
)

print("5. Custom DateTime")
print(custom_datetime)
print()


# ------------------------------------------------
# 6. Extract Individual Components
# ------------------------------------------------

print("6. Extract Components")

print("Year :", current_datetime.year)
print("Month:", current_datetime.month)
print("Day  :", current_datetime.day)

print("Hour :", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)

print()


# ------------------------------------------------
# 7. Format Date and Time using strftime()
# ------------------------------------------------

print("7. Formatted Date and Time")

formatted = current_datetime.strftime("%d-%m-%Y %H:%M:%S")

print(formatted)
print()


# ------------------------------------------------
# Common Formatting Codes
# ------------------------------------------------

print("Day Name   :", current_datetime.strftime("%A"))
print("Month Name :", current_datetime.strftime("%B"))
print("Year       :", current_datetime.strftime("%Y"))
print("12 Hour    :", current_datetime.strftime("%I:%M %p"))

print()


# ------------------------------------------------
# 8. Convert String to DateTime
# ------------------------------------------------

date_string = "15-06-2025 10:30:00"

converted = datetime.datetime.strptime(
    date_string,
    "%d-%m-%Y %H:%M:%S"
)

print("8. String to DateTime")
print(converted)
print()


# ------------------------------------------------
# 9. Date Arithmetic using timedelta
# ------------------------------------------------

print("9. Date Arithmetic")

today = datetime.datetime.now()

# Add 10 days
future_date = today + datetime.timedelta(days=10)

# Subtract 5 days
past_date = today - datetime.timedelta(days=5)

print("Today      :", today)
print("After 10 Days:", future_date)
print("Before 5 Days:", past_date)

print()


# ------------------------------------------------
# 10. Difference Between Two Dates
# ------------------------------------------------

date1 = datetime.date(2025, 1, 1)
date2 = datetime.date(2025, 12, 31)

difference = date2 - date1

print("10. Difference Between Dates")
print("Days:", difference.days)

print()


# ------------------------------------------------
# 11. Calculate Age Example
# ------------------------------------------------

birth_date = datetime.date(2000, 5, 20)

today = datetime.date.today()

age_days = (today - birth_date).days

age_years = age_days // 365

print("11. Age Calculation")
print("Approximate Age:", age_years, "years")

print()


# ------------------------------------------------
# 12. Timestamp Example
# ------------------------------------------------

timestamp = datetime.datetime.now().timestamp()

print("12. Unix Timestamp")
print(timestamp)

print()


# ------------------------------------------------
# End of Program
# ------------------------------------------------

print("DateTime Demonstration Completed Successfully!")