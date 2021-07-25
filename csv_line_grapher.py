import matplotlib.pyplot as plt

with open(input("CSV file to read: ")) as input_csv_file:
    labels = input_csv_file.readline().strip().split(",")
    x_points, y_points = [], []
    for line in input_csv_file:
        x, y = line.split(",")
        x_points.append(x)
        y_points.append(y)

print(labels, x, y)

plt.xlabel(labels[0])
plt.ylabel(labels[1])
plt.plot(x_points, y_points)
plt.show()
