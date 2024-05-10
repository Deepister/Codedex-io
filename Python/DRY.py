#“Don't Repeat Yourself” (DRY) is a principle in software development aimed at reducing repetition 
# and writing good clean code. Functions play a big part.



# Creating a list of items needed for a dog
dog_items = ["dog food", "water bowl", "leash", "collar", "dog bed", "toys", "treats"]

# Using built-in functions

# 1. len() - Returns the number of items in a list
num_items = len(dog_items)
print("Number of items needed for a dog:", num_items)

# 2. insert() - Inserts an item at a specified position in a list
dog_items.insert(2, "brush") # Inserts "brush" at index 2
print("Inserted 'brush' into the list of dog items:", dog_items)

# 3. pop() - Removes and returns the item at the specified index (default is the last item)
removed_item = dog_items.pop(4) # Removes the item at index 4, which is "dog bed"
print("Removed item from the list:", removed_item)
print("Updated list after removing 'dog bed':", dog_items)

# 4. sort() - Sorts the items in a list in ascending order (or based on custom criteria)
dog_items.sort()
print("Sorted list of dog items:", dog_items)

# 5. reversed() - Returns an iterator that yields items in reverse order
reversed_items = list(reversed(dog_items)) # Converting the reversed iterator to a list
print("Reversed list of dog items:", reversed_items)
