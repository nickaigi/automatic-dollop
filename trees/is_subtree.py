def are_identical(root_one, root_two):
      if root_one is None and root_two is None:
          return True
      if root_one is None or root_two is None:
          return False
      return root_one.value == root_two.value and are_identical(root_one.left, root_two.left) and are_identical(root_one.right, root_two.right)


  def isSubtree(t1, t2):
      if t2 is None:
          return True
      if t1 is None:
          return False
      if are_identical(t1, t2):
          return True
      return isSubtree(t1.left, t2) or isSubtree(t1.right, t2)
