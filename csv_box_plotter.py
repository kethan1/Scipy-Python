import matplotlib.pyplot as plt

with open("testcsv_box_plotter.csv") as input_file:
    headers = input_file.readline().strip().split(",")
    input_data = {category: [] for category in headers}
    for line in input_file:
        values = line.strip().split(",")
        for index, value in enumerate(values):
            input_data[headers[index]].append(int(value))

print(input_data)

figure = plt.figure(1, figsize=(9, 6))
axes = figure.add_subplot(111, title="Box Plot Grapher")
axes.boxplot(list(input_data.values()))
axes.set_xticklabels(headers)
plt.show()
