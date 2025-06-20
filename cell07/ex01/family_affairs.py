def find_the_redheads(family):
    # Use filter to find keys (first names) where value (hair color) is "red"
    redheads = list(filter(lambda name: family[name].lower() == "red", family))
    return redheads

if __name__ == "__main__":
    # Example dictionary
    family_members = {
        "Alice": "blonde",
        "Bob": "red",
        "Charlie": "brown",
        "Daisy": "red",
        "Eve": "black"
    }

    redhead_list = find_the_redheads(family_members)
    print("Red-haired family members:", redhead_list)