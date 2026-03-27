# Creation
user = {"name": "Alice", "role": "Engineer", "level": 4}
empty_dict = dict()

# Adding and Updating
user["location"] = "Ankara"       # Adds a new key-value pair
user["level"] = 5                 # Updates an existing key

# Removal
role = user.pop("role")           # Removes the key and returns its value
del user["location"]              # Deletes the key-value pair entirely
user.clear()                      # Empties the entire dictionary


data = {"a": 1, "b": 2, "c": 3}

# Iterating keys (Default behavior)
for key in data:
    print(key)

# Iterating values
for value in data.values():
    print(value)

# Iterating both (The Pythonic way)
for key, value in data.items():
    print(f"{key} maps to {value}")


names = ["Alice", "Bob", "Charlie"]
# Map names to their string lengths
name_lengths = {name: len(name) for name in names}

# Filtering a dictionary
scores = {"Alice": 85, "Bob": 59, "Charlie": 92}
passing_scores = {k: v for k, v in scores.items() if v >= 60}

defaults = {"theme": "light", "port": 8080}
custom = {"port": 3000, "debug": True}

final_config = defaults | custom  # custom overwrites defaults where they overlap

final_config_old = {**defaults, **custom}

valid_dict = {(1, 2): "point A"}  # Tuples are immutable, this works!
# invalid_dict = {[1, 2]: "point A"} # TypeError: unhashable type: 'list'


dict_a = {"x": 1, "y": 2}
dict_b = {"y": 3, "z": 4}

# Find common keys instantly using Set Intersection (&)
common_keys = dict_a.keys() & dict_b.keys() # {'y'}


user_profile = {"name": "Alice", "role": "Dev", "active": True}
new_data = {"role": "Senior Dev", "location": "Ankara"}

user_profile.update(new_data)
# user_profile is now: {'name': 'Alice', 'role': 'Senior Dev', 'active': True, 'location': 'Ankara'}
print(user_profile)