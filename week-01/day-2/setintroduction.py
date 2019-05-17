"""
Create a set
Add at least 5 members to the set
Remove at most 2 members from the set
Iterate over the set and print its members
Remove 482 from the set if it is present
Remove 42 from the set even if it is not present
"""
set1 = {1,2,3,4,5}
set1.remove(1)
set1.remove(2)

for i in set1:
    print(i)
if 482 in set1:
    set1.remove(482)

set1.remove(42)