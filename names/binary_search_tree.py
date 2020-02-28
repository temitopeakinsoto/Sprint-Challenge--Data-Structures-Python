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