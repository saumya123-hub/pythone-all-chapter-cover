l = [1,2,3,4,5,6,7,8,1,1]
print(l)
l.append(9)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(1))
print(l)
print(l.index(1))
print(l.index(8))
print(l.index(9))
print(l.count(9))
m = l.copy()
m[0]=0
print(l)
l.insert(1,899)
print(l)
m = [900,1000,1100]
l.extend(m)
print(l)
color1 = ["red","blue","green","yello","pink"]
color2 = ["black","light pink","light gulabi"]
print(color1+color2)
print(color1*color2)
