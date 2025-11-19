# Dictionaries in python is a way to stroe data in key-value pairs

month_conversion = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    10: "July",
    "aug": "August",
    "aug": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December",
}

print(month_conversion["nov"])  # Output: November
print(month_conversion.get("apr")) # The thing about this get method is that if the key is not found it will return None instead of an error , and we can pass a default value.
print(month_conversion.get(10)) # The thing about this get method is that if the key is not found it will return None instead of an error , and we can pass a default value.
print(month_conversion.get("aprl", "Not a valid key"))  # Output: Not a valid key


print(month_conversion.get("aug"))