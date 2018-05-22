from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
from statkraft.ltm.scripting import plot_ts
import matplotlib.pyplot as plt
from statkraft.ltm.domain_model.area_aggregate import MultiAreaAggregate

rr = RunRepository()
run_id = rr.find_closest_operational_run(sa.utctime_now())
run = rr.recreate(run_id=run_id)

start = run.start_utc
time_axis = run.time_axis

ger = run.model.areas["Tyskland"]
pol = run.model.areas["Polen"]
sweden = run.model.countries["Sweden"]

pol_ger = MultiAreaAggregate(tag="GerPol",parent=run.model,name="GerPol",aggregation_list=[ger,pol])


exp = pol_ger.export.to(sweden).mean(time_axis=time_axis, unit="GWh")
gross_exp = pol_ger.gross_export.to(sweden).mean(time_axis=time_axis,unit="GWh")

plot_ts(exp)
plot_ts(gross_exp)
plt.show(block=True)