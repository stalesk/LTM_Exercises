from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
from statkraft.ltm.scripting import plot_ts, plot_percentiles
import matplotlib.pyplot as plt

t0 = sa.utctime_now() - sa.Calendar.WEEK

rr = RunRepository()

run_id = rr.find_closest_operational_run(t0)

run = rr.recreate(run_id = run_id)

sts = run.model.areas["Sorland"].aggregated_hydro.bypass
time_axis = sa.TimeAxis(run.start_utc, sa.Calendar.DAY, 100)
ts_vec = sts.mean(time_axis = time_axis, unit = 'MW', years = [1931, 1945])

plot_ts(ts_vec)