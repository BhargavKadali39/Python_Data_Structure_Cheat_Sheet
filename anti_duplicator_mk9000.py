List_1 = [1,1,1,2,3,4,4,4,5,5,6,6]

'''
# The old method

List_2 = []

for i in List_1:
  if i not in List_2:
    List_2.append(i)
    
print(List_2)

# Still this old method is faster than the other.
# Execution time is: 0.008489199999999975
# That much doesn't matter much,not in the case while working with big amount of data.
'''

# Removing Duplicates using set() and List() methods.

List_3 = list(set(List_1))
print(List_3)

# Execution time is: 0.011315100000000022
