def print_user(**kwargs):
    for key in kwargs.keys():
        print(f"{key}")

# Example usage:
print_user(name="Alice", age=12, hobby="Drawing", city="US")
