from collections import Counter
perimeter=[]
for i in range(1,500):
    for j in range(i,500):
        z=(i**2+j**2)**(1/2)
        if int(z) == z and (i+j+z) <= 1000:
            perimeter.append((i+j+z))

p = Counter(perimeter)
print(p.most_common(1)[0])
