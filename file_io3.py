# with open("test.csv") as file:
#     for line in file:
#         print("---------------------")
#         print("|" + "|".join(line.split(",")).strip() + "|")

with open("test2.csv") as file:
    rows = [row.strip() for row in file.readline().split(",")]
    data = {row: [] for row in rows}
    for line in file:
        for index, item in enumerate(line.split(",")):
            data[rows[index]].append(float(item.strip()))
    for key, value in data.items():
        print(f"Column: {key}, min: {min(value)}, max: {max(value)}, mean: {sum(value) / len(value)}")
