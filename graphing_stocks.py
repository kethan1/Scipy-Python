import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.lines import Line2D
import json
import stocks

with open("apiKeys.json") as api_keys:
    api_key = json.load(api_keys)["rapid_api_key"]["api_key"]


fig1 = plt.figure()


def get_data(symbol):
    stock_history = stocks.stock_history(symbol=symbol, api_key=api_key, output_date_format="%b %d, %Y")

    y_values = np.asarray([(price['high'] + price['low']) / 2 if 'high' in price and 'low' in price else None for price in stock_history.values()][::-1])
    for index, y_value in enumerate(y_values):
        if y_value is None and index != 0:
            y_values[index] = y_values[index - 1]

    dates = list(stock_history.keys())[::-1]

    if y_values[0] is None:
        y_values = y_values[1:]
        dates = dates[1:]

    return [dates, y_values]


def graph_stock(dates, y_values):
    x = np.asarray(range(1, len(dates) + 1))
    z = np.asarray([i - j for i, j in zip(y_values[:-1], y_values[1:])])

    # Create a colormap for red, green and blue and a norm to color
    # f' < -0.5 red, f' > 0.5 blue, and the rest green
    cmap = ListedColormap(['g', 'b', 'r'])
    norm = BoundaryNorm([-100, -0.5, 0.5, 100], cmap.N)

    # Create a set of line segments so that we can color them individually
    # This creates the points as a N x 1 x 2 array so that we can stack points
    # together easily to get the segments. The segments array for line collection
    # needs to be numlines x points per line x 2 (x and y)
    # points = np.array([x, y_values]).T.reshape(-1, 1, 2)
    points = np.array([x, y_values]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # Create the line collection object, setting the colormapping parameters.
    # Have to set the actual values used for colormapping separately.
    lc = LineCollection(segments, cmap=cmap, norm=norm)
    lc.set_array(z)
    lc.set_linewidth(3)

    plt.gca().add_collection(lc)

    plt.xlim(0, len(x)-1)
    plt.ylim(min(y_values), max(y_values))
    plt.xticks(x[::30], dates[::30], rotation=40)
    plt.tight_layout()
    return lc


def graph_many_stocks(*args):
    companies = [get_data(symbol) for symbol in args]
    for company in companies:
        graph_stock(*company)

    lines = [Line2D([0], [0], color='k', linewidth=3) for _ in the_stocks]
    plt.legend(lines, [f'{args[index]}: {min(company[1])} - {max(company[1])}' for index, company in enumerate(companies)])
    plt.ylim(min([min(company[1]) for company in companies]), max([max(company[1]) for company in companies]))


# the_stocks = ['MSFT', 'AAPL', 'SHLDQ', 'AMZN']
the_stocks = list(map(lambda x: x.strip(), input('Please enter a list of comma seperate stocks: ').split(',')))
graph_many_stocks(*the_stocks)

plt.show()
