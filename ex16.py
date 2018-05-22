from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
from statkraft.ltm.scripting import plot_ts,plot_percentiles
from statkraft.ltm.domain_model.detailed_hydro import MultiAreaDetails
import matplotlib.pyplot as plt

rr = RunRepository()
run_id = rr.find_closest_operational_run(sa.utctime_now())
run = rr.recreate(run_id=run_id)

calendar = sa.Calendar()
dt = calendar.HOUR * 6
start = run.start_utc
end = start + calendar.WEEK * 5



n = calendar.diff_units(start,end,dt)
time_axis = sa.TimeAxis(calendar,start,dt,n)

se1_hyd = run.model.market.areas["SE1"].detailed_hydro
se2_hyd = run.model.market.areas["SE2"].detailed_hydro
norswe = MultiAreaDetails(parent=run.model, areas=[se1_hyd,se2_hyd])

hyd_prod = norswe.production.percentiles(time_axis=time_axis,unit="MW")

plot_ts(hyd_prod)
plt.show(block=True)
