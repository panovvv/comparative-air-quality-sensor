from datetime import datetime
from random import randint

import pandas
import seaborn
from matplotlib import pyplot
from matplotlib.dates import DateFormatter

X_WIDTH = 60
X_FREQ = "10s"

x = []
y1 = []
y2 = []


def handle_close(evt):
    print("Closed the window!")
    exit(0)


def gui_loop(redraw_period):
    seaborn.set()

    # interactive mode on - non blocking rendering call
    pyplot.ion()

    (line1,) = pyplot.plot_date(x, y1, "-", xdate=True, label="d1")
    (line2,) = pyplot.plot_date(x, y2, "-", xdate=True, label="d2")
    pyplot.legend()
    pyplot.yticks(list(range(0, 110, 10)))
    pyplot.gca().set_ylim(0, 110)
    pyplot.gca().xaxis.set_major_formatter(DateFormatter("%d %H:%M:%S"))
    fig = pyplot.gcf()
    fig.canvas.set_window_title("Comparative air quality sensor")
    fig.canvas.manager.full_screen_toggle()

    pyplot.show()

    pyplot.gca().figure.canvas.mpl_connect("close_event", handle_close)
    while True:
        x_end = datetime.now()
        x_start = datetime.fromtimestamp((datetime.timestamp(x_end) - X_WIDTH))
        x_ticks = pandas.date_range(x_start, x_end, freq=X_FREQ)

        pyplot.xticks(x_ticks)
        pyplot.gca().set_xlim(x_start, x_end)
        pyplot.gcf().autofmt_xdate()

        x.append(x_end)
        y1.append(randint(0, 100))
        y2.append(randint(0, 100))
        if len(x) == X_WIDTH:
            x.pop(0)
            y1.pop(0)
            y2.pop(0)
        line1.set_xdata(x)
        line1.set_ydata(y1)
        line2.set_xdata(x)
        line2.set_ydata(y2)
        pyplot.pause(redraw_period)
