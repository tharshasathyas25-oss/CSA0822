import copy
rows, cols = 3, 4
bad = [[0] * cols] * rows
bad[0][1] = 7
good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7
print("bad :", bad)
print("good:", good)
print(bad[0] is bad[1], good[0] is good[1])
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}
print(stops[(13.0418, 80.2341)])
a = [1, 2, 3]
b = a
b[0] = 10
print("Aliasing:", a)
c = [1, 2, 3]
d = copy.copy(c)
d[0] = 20
print("Original:", c)
print("Shallow Copy:", d)
x = [[1, 2], [3, 4]]
y = copy.deepcopy(x)
y[0][0] = 100
print("Original:", x)
print("Deep Copy:", y)
coordinates = [(10, 20), (30, 40)]
for lat, lon in coordinates:
    print("Latitude:", lat, "Longitude:", lon)
