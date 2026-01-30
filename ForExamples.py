#print 1-10


for i in range(-10,10, 2):
    print(i)

for i in range(1,11):
    for j in range(i,11):
        print(f"{i} x {j} = {i*j}")
    print()