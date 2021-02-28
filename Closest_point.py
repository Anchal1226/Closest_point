import math
n = int(input("Enter n - "))
x_cords = []
y_cords = []
for i in range(0,n):
    x, y = input("Enter a point - ").split()
    x_cords.append(int(x))
    y_cords.append(int(y))
xn,yn = input("Enter the point to compare with - ").split()
xn = int(xn)
yn = int(yn)

diffs_x = []
diffs_y = []

for x in x_cords:
    diffx = abs(x-xn)
    diffx = diffx**2
    diffs_x.append(diffx)
    
for y in y_cords:
    diffy = abs(y-yn)
    diffy = diffy**2
    diffs_y.append(diffy)

dists = []
for i in range(0,n):
    dists.append(math.sqrt((diffs_y[i]+diffs_x[i])))
min_dist = min(dists)
index = dists.index(min_dist,0,n)
closest_point = index+1
print("Point "+str(closest_point)+" is closest to the label")
