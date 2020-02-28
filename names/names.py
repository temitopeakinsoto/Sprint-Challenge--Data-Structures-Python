import time
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree
    def insert(self, value):
      if value < self.value:
        if self.left is None:
          self.left = BinarySearchTree(value)
        else:
          # if something is already there, recurse
          self.left.insert(value)
      elif value >= self.value:
        if self.right is None:
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)
      return self
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
          return True
        if target < self.value:
          if not self.left:
            return False
          else:
            return self.left.contains(target)
        else:
          if not self.right:
            return False
          else:
            return self.right.contains(target)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

binary = BinarySearchTree('names')
for name1 in names_1:
  binary.insert(name1)

for name2 in names_2:
  if binary.contains(name2):
    duplicates.append(name2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
