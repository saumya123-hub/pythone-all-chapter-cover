#  union and update
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union (s2))
s1.update(s2)
print(s1 , s2)


# intersection and update
s = { 2,3,4,5,6,7,8}
s3 = {7,8,9,10}
print(s.intersection(s3))
s.intersection_update(s3)
print(s)

#  symmetric_difference
s = { 2,3,4,5,6,7,8}
s3 = {7,8,9,10}
print(s.symmetric_difference(s3))


# difference and difference_update
s = { 2,3,4,5,6,7,8}
s1 = {7,8,9,10}
print(s.difference(s1))


# disjoint set koi bhi join n ho usko disjoin kahte hai
s = { 2,3,4,5,6}
s1 = {7,8,9,10}
print(s.isdisjoint(s1))  


# issuperset() mean s1 me jtna bhi number hai wo s me aa jaye usko issuperset kahte hai
s = { 2,3,4,5,6,7,8,9}
s1 = {7,8,9,10}
print(s.issuperset(s1))
print(s1.issubset(s))




