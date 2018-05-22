from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
from statkraft.ltm.state import quantity
from statkraft.ltm.scripting import plot_ts
import matplotlib.pyplot as plt
from statkraft.ltm.io.converter import to_pandas

rr = RunRepository()
t0 = sa.utctime_now() - sa.Calendar.DAY * 2
res = rr.search(labels=["operational","norway"], created_from=t0)
areas = ["NO1", "NO2", "NO5"]
tsv = quantity(sa.TsVector(), "GWh")

tot_cons_list = []
legend_list = []
for key in res.keys():
    run_info = res[key]
    run = rr.recreate(run_id=key)
    legend_list.append(key)
    time_axis = sa.TimeAxis(sa.utctime_now(), sa.Calendar.DAY, 365)
    tot_cons = quantity(sa.TsVector(), "GWh")
    for key1 in run.model.market.areas.keys():
        this_area = run.model.market.areas[key1]
        if key1 in areas:
            cons = this_area.consumption.mean(unit="GWh", time_axis = time_axis)
            tot_cons += cons
    tot_cons_list.append(tot_cons)


diff_cons = tot_cons_list[0] - tot_cons_list[1]
tsv.extend(diff_cons.magnitude)

df, pip = to_pandas(tsv)
df = df.magnitude
df.columns = ["Diff"] + [df.columns[-1]]
df.to_csv("diff_consumption.csv")

#tsv.extend(tot_cons_list[0].magnitude)
#tsv.extend(tot_cons_list[1].magnitude)
#plot_ts(tsv)
#plot_ts(tot_cons_list[1].magnitude)
#plt.legend(["Diff"])
#plt.show(block=True)




