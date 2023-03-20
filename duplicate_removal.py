"""
This program is meant to remove every duplicate in a list
"""
if __name__ == "__main__":
    
    fridge = ["bottle water", 6, "apples", "oranges", "pepper", "yoghurt", "meat", 56, "oranges", "bottle water"]

    unique_fridge = [ ]
    for item in fridge:
        if item not in unique_fridge:
            unique_fridge.append(item)
        else:
            print(f"{item} is duplicated")
    print (unique_fridge)