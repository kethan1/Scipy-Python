import ast
import matplotlib.pyplot as plt


class InvalidConfig(Exception):
    pass


filename = input("CSV file: ")
with open(filename) as input_file:
    headers = input_file.readline().strip().split(",")
    category_value = list(map(int, input_file.readline().strip().split(",")))
    config = input_file.readline()
    if config.startswith("!!config; "):
        try:
            config = ast.literal_eval(config[9:].strip())
        except:
            raise InvalidConfig("Invalid config dictionary provided.")
    else:
        config = {}
    if "legend" not in config:
        config["legend"] = True
    if "colors" not in config or not config["colors"]:
        config["colors"] = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"]
    if "exploded" not in config or not config["exploded"]:
        config["exploded"] = [0.1, 0, 0, 0]
    if "shadow" not in config:
        config["shadow"] = True
    print(config)

color_swatches = plt.pie(
    category_value,
    labels=headers,
    autopct="%1.1f%%",
    explode=config["exploded"],
    shadow=config["shadow"],
    colors=config["colors"]
)[0]

if config["legend"]:
    plt.legend(color_swatches, headers, loc="best")
plt.title(filename.strip(".csv"))
plt.show()
