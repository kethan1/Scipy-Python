import matplotlib.pyplot as plt

slice_names = ["Python", "Java", "C#", "C"]
slice_sizes = [50, 90, 20, 14]

color_swatches = plt.pie(
    slice_sizes,
    labels=slice_names,
    autopct="%1.1f%%",
    explode=[0.1, 0, 0, 0],
    shadow=True,
    colors=["#ff0000", "#00ff00", "#0000FF", "#FFFF00"]
)[0]

plt.legend(color_swatches, slice_names, loc="best")
plt.show()
