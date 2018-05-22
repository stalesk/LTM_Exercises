from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
import matplotlib.pyplot as plt
from statkraft.ltm.scripting import plot_ts, plot_percentiles

calendar = sa.Calendar("Europe/Oslo")
dt = calendar.HOUR * 6
start = calendar.time(2018,5,1,0,0,0)
end = calendar.time(2019,5,1,0,0,0)
n = calendar.diff_units(start,end,dt)
time_axis = sa.TimeAxis(start,dt,n)

