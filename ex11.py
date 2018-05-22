from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
from statkraft.ltm.scripting import plot_ts
from statkraft.ltm.state import quantity
import matplotlib.pyplot as plt

rr = RunRepository()
t0 = sa.utctime_now()
run_id = rr.find_closest_operational_run(t0)
run = rr.recreate(run_id = run_id)

calendar = sa.Calendar("Europe/Oslo")
dt = calendar.WEEK
start = calendar.time(2018,9,1,0,0,0)
end = calendar.time(2021,9,1,0,0,0)
n = calendar.diff_units(start,end,dt)
time_axis = sa.TimeAxis(start,dt,n)

l_reservoirs = {}
legend_list = []
for key in run.model.areas.keys():
    emps_area = run.model.areas[key]
    max_volume = 0
    max_tag = None

    if not emps_area.detailed_hydro is None:
        for res_key in emps_area.detailed_hydro.reservoirs.keys():
            res = emps_area.detailed_hydro.reservoirs[res_key]
            res_volume = res.max_volume.magnitude
            if res_volume > max_volume:
                max_volume = res_volume
                max_tag = res.local_tag
        if max_tag is not None:
            max_res = emps_area.detailed_hydro.reservoirs[max_tag]
            l_reservoirs[key] = max_res
        else:
            print("hæh?")

tsv = quantity(sa.TsVector(), "m**3")
print(l_reservoirs)
for key in l_reservoirs.keys():
    obj_res = l_reservoirs[key]
    legend_list.append(obj_res.name)
    obj_res_mean_volume = obj_res.volume.mean(time_axis = time_axis, unit = "m**3")
    tsv.extend(obj_res_mean_volume.magnitude)

plot_ts(tsv)
plt.legend(legend_list)
plt.show(block=True)