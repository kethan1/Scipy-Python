import matplotlib.pyplot as plt

figure = plt.figure(1, figsize=(9, 6))
axes = figure.add_subplot(111, title="Box plots are cool")
axes.boxplot([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 6, 9, 10]])
axes.set_xticklabels(['Dogs', 'Cats', 'Bats'])
plt.show()
