from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
from statkraft.ltm.domain_model.area_aggregate import MultiAreaAggregate
from statkraft.ltm.io.converter import to_pandas

rr = RunRepository()
run_id = rr.find_closest_operational_run(sa.utctime_now())
run = rr.recreate(run_id=run_id)

cal = sa.Calendar("Europe/Oslo")
dt = cal.MONTH
start = run.start_utc
end = run.time_axis.total_period().end
n = cal.diff_units(start,end,dt)
time_axis = sa.TimeAxis(start,dt,n)

ger = run.model.areas["Tyskland"]
pol = run.model.areas["Polen"]
years = run.run_info.scenario_years

pol_ger = MultiAreaAggregate(tag="GerPol",parent=run.model,name="GerPol",aggregation_list=[ger,pol])

ts_vec = pol_ger.consumption(time_axis=time_axis,unit="GWh")


df, pip = to_pandas(ts_vec)
df = df.magnitude
df.columns = years + [df.columns[-1]]
df.to_csv("consumption_pol_ger.csv")

