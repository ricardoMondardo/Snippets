# Have the function TreeConstructor(strArr) take the array of strings stored in strArr, which will contain pairs of integers in the following format: (i1,i2), where i1 represents a child node in a tree and the second integer i2 signifies that it is the parent of i1. For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the following tree:
# which you can see forms a proper binary tree. Your program should, in this case, return the string true because a valid binary tree can be formed. If a proper binary tree cannot be formed with the integer pairs, then return the string false. All of the integers within the tree will be unique, which means there can only be one node in the tree with the given integer value.

def TreeConstructor(strArr):

  parents = {}
  chilrens = {}

  for i in strArr:

    children = i.replace('(','').replace(')','').split(',')[0]
    parent = i.replace('(','').replace(')','').split(',')[1]

    if parent in parents:
      parents[parent].append(children)
      if len(parents[parent]) > 2:
        return 'false'
    else:
      parents[parent] = [children]
     
    if children in chilrens:
      chilrens[children].append(parents)
      if len(chilrens[children]) > 1:
        return 'false'
    else:
      chilrens[children] = [parent]


  return 'true'

# keep this function call here 
print(TreeConstructor(["(2,3)", "(1,2)", "(4,9)", "(9,3)", "(12,9)", "(6,4)"]))