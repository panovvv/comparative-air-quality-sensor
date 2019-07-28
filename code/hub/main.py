import pandas as pd
import seaborn as sns
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter
from random import randint

X_WIDTH = 60
X_FREQ = '10s'


def handle_close(evt):
    print('Closed the window!')
    exit(0)


# sns.set()
sns.set(rc={'figure.figsize': (11, 4)})

# interactive mode - non blocking rendering call
plt.ion()

x = []
y1 = []
y2 = []
line1, = plt.plot_date(x, y1, '-', xdate=True, label="d1")
line2, = plt.plot_date(x, y2, '-', xdate=True, label="d2")
plt.legend()
plt.yticks(list(range(0, 110, 10)))
plt.gca().set_ylim(0, 110)
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M:%S'))

plt.show()

plt.gca().figure.canvas.mpl_connect('close_event', handle_close)

while True:

    xend = datetime.now()
    xstart = datetime.fromtimestamp((datetime.timestamp(xend) - X_WIDTH))
    xticks = pd.date_range(xstart, xend, freq=X_FREQ)

    plt.xticks(xticks)
    plt.gca().set_xlim(xstart, xend)
    plt.gcf().autofmt_xdate()

    x.append(xend)
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
    plt.pause(1)
