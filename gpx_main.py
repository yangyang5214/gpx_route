from datetime import datetime
from xml.dom.minidom import parse

import matplotlib.pyplot as plt
import pytz
from matplotlib import animation


def utc_to_local(utc_time_str, utc_format='%Y-%m-%dT%H:%M:%SZ'):
    local_tz = pytz.timezone('Asia/ShangHai')  # 定义本地时区
    local_format = "%Y-%m-%d %H:%M:%S"  # 定义本地时间format
    utc_dt = datetime.strptime(utc_time_str, utc_format)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_dt.strftime(local_format)


def main():
    dom = parse('6884490616.gpx')
    data = dom.documentElement
    trkpts = data.getElementsByTagName('trkpt')
    x_ys = []
    min_x = float('inf')
    min_y = float('inf')
    for trkpt in trkpts:
        lat = trkpt.getAttribute("lat")
        lon = trkpt.getAttribute("lon")
        x = int(float(lat) * 1_000_000)
        y = int(float(lon) * 1_000_000)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        x_y = [x, y]
        x_ys.append(x_y)

    xs = []
    ys = []
    for _ in x_ys:
        xs.append(_[0] - min_x)
        ys.append(_[1] - min_x)

    fig, axs = plt.subplots()

    axs.plot(ys, xs, color='orange')

    line, = axs.plot([], [], 'ro')

    def _func(index):
        line.set_data(ys[index], xs[index])
        return line,

    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    ani = animation.FuncAnimation(fig, _func, frames=len(xs), interval=1)
    ani.save('dsh.mp4', fps=130)
    # plt.show()


if __name__ == '__main__':
    main()
