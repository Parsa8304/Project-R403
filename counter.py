Person ={
    "age" : [15 , 45],
    "weight": [60 , 120],
    "Height" : [150 , 160,180 , 200],
    "Skin" : ["bonze", "sand"],
    "Hair": [ "black", "brown"],
    "Glasses": False,
    "Mask" : True
    
}

def Watch(Person):
    percent = []

    # Iterate over the dictionary to check truthy values
    for key, value in Person.items():
        if value:  # Add to percent if the value is truthy
            percent.append(1)
    
    # Determine familiarity based on the length of percent
    if len(percent) > 5:
        print("Familiar")
    elif 2 < len(percent) <= 5:
        print("Maybe familiar")
    else:
        print("Unfamiliar")
    
    return percent

# Example usage
result = Watch(Person)
print("Truthy count:", len(result))


mystr = 'Parsa.  Khezli'
print(mystr.split("."))