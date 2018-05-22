from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
from statkraft.ltm.scripting import plot_ts, plot_percentiles
from matplotlib import pyplot as plt
from statkraft.ltm.io.converter import to_pandas
import pandas as pd

rr = RunRepository()
t0 = sa.utctime_now()
run_id = rr.find_closest_operational_run(t0)

run = rr.recreate(run_id = run_id)
time_axis = sa.TimeAxis(run.start_utc, sa.Calendar.DAY,365)


prices = {}
df_tot = pd.DataFrame()

for area_name, area in run.model.areas.items():
    df, pip = to_pandas(area.power_price.mean(time_axis = time_axis))
    prices[area_name] = df.magnitude



