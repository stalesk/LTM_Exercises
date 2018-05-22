from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
from statkraft.ltm.scripting import plot_ts, plot_percentiles
from matplotlib import pyplot as plt
from statkraft.state import quantity

tsv = quantity(sa.TsVector(), "EUR/MWh")

rr = RunRepository()
t0 = sa.utctime_now()
run_id = rr.find_closest_operational_run(t0)

run = rr.recreate(run_id = run_id)
time_axis = sa.TimeAxis(run.start_utc, sa.Calendar.DAY,365)

prices = {}

legend_list = []
for area_name, power_price in run.model.areas.items():
    legend_list.append(area_name)
    tsv.append(area.power_price.mean(time_axis=time_axis).magnitude[0])
    plot_ts(power_price)

plt.legend(legend_list)
plt.show(block=True)



