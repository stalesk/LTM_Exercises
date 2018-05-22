import matplotlib.pyplot as plt
import shyft.api as sa
from statkraft.ltm.io.run_repository import RunRepository
from statkraft.ltm.scripting import plot_ts

calendar = sa.Calendar("Europe/Oslo")
utc_start = calendar.time(2018, 7, 1)
time_axis = sa.TimeAxis(calendar, utc_start, calendar.QUARTER, 1)

now = sa.utctime_now()
then = now - calendar.WEEK

rr = RunRepository()
rid1 = rr.find_closest_operational_run(now)
rid2 = rr.find_closest_operational_run(then)

run1 = rr.recreate(run_id=rid1)
run2 = rr.recreate(run_id=rid2)

sp1 = run1.model.market.areas["NO2"].power_price.mean(time_axis=time_axis)
sp2 = run2.model.market.areas["NO2"].power_price.mean(time_axis=time_axis)

plot_ts(sp1 - sp2)
plt.legend([f"NO2 price difference: run[{rid1}] - run[{rid2}]"])
