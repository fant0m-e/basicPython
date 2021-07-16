monthConversions = { # key (can be a number) can't have duplicates. "key": "value pair",
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"]) # calls out November
print(monthConversions.get("Dec")) # also calls out a key's value pair
print(monthConversions.get("Luv", "Not a valid key")) # pass in a message
