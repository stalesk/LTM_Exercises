import matplotlib.pyplot as plt
import shyft.api as sa
from statkraft.ltm.io.run_repository import RunRepository
from statkraft.ltm.scripting import plot_ts
rr = RunRepository()
rid = rr.find_closest_operational_run(sa.utctime_now())
run = rr.recreate(run_id=rid)

time_axis = sa.TimeAxis(run.start_utc, sa.Calendar.DAY, 52*7)

prices = {}

for area_name, area in run.model.areas.items():
    prices[area_name] = area.power_price.mean(time_axis=time_axis)

legend_list = []
for area_name, power_price in prices.items():
    legend_list.append(area_name)
    plot_ts(power_price)
plt.legend(legend_list)
plt.show(block=True)

