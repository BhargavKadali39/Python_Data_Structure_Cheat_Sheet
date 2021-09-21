List_1 = [1,1,1,2,3,4,4,4,5,5,6,6]

'''
# The old method

List_2 = []

for i in List_1:
  if i not in List_2:
    List_2.append(i)
    
print(List_2)

# This method is a no no.
# For beginners it's ok to learn like this but don't continue like this!
'''

# Removing Duplicates using set() and List() methods.

List_3 = list(set(List_1))
print(List_3)
