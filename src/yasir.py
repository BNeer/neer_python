# Lists
musketeers = ['Athos', 'Porthos', 'Aramis']

print(musketeers[0])
print(musketeers[2])
print(len(musketeers))

## list methods 
musketeers.append('Yasir')
musketeers.insert(2, 'Neeraj')
musketeers.extend(['Ankita', 'Levina'])
musketeers.remove('Neeraj')
musketeers.pop(1)
print(musketeers)


# list manipulation
nums = [1, 2, 3]
mix = [musketeers, nums]
mix
mix[1][2]

# --------------------------------------
# Dictionaries:
person = {
    "first_name": "Jason",
    "last_name": "Derulo",
    "age": 50,
    "city": "New York",
    "email": "jderulo@example.com"
}

# Accessing dictionary
print("First Name:", person["first_name"])
print("Last Name:", person["last_name"])
print("Age:", person["age"])
print("City:", person["city"])
print("Email:", person["email"])

#---------------------------------
# List Comprehensions:

even_nums = [x for x in range(1, 11) if x % 2 == 0]
even_nums

# strings
words = ["dell", "is", "an", "amazing", "laptop"]
uppercase_words = [word.upper() for word in words]
uppercase_words

# -----------------------------

# Filtering and Transforming Data: 
# Sample customer data
customer_data = {
    "customer1": {"name": "Alice", "purchases": [100, 150, 200]},
    "customer2": {"name": "Bob", "purchases": [50, 75, 80]},
    "customer3": {"name": "Charlie", "purchases": [300, 400, 500]},
    "customer4": {"name": "David", "purchases": [75, 90, 110]},
}

mega_spend = 200

golden_customers = {
    customer_id: {
        "name": data["name"],
        "total_purchases": sum(data["purchases"]),
    }
    for customer_id, data in customer_data.items()
    if sum(data["purchases"]) > mega_spend
}

# filtered and transformed data
for customer_id, data in golden_customers.items():
    print(f"Customer {customer_id}: {data['name']} (->: ${data['total_purchases']})")

#----------------------------------------------------

# Nested List Comprehensions: Discuss nesting list comprehensions for more complex operations.
cities = ['London', 'Reading', 'Exeter', 'York', 'Leeds']
temps = {city: [0 for _ in range(7)] for city in cities}
temps