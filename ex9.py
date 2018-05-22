from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
from statkraft.ltm.state import quantity
from statkraft.ltm.io.converter import to_pandas

rr = RunRepository()
t0 = sa.utctime_now() - sa.Calendar.DAY

run_id = rr.find_closest_operational_run(t0)
run = rr.recreate(run_id = run_id)
areas = ["SE1", "SE2", "SE3","SE4"]
energy_inflow = quantity(sa.TsVector(), "GWh")
time_axis = sa.TimeAxis(sa.utctime_now(), sa.Calendar.MONTH, 24)

years = run.run_info.scenario_years

for key in run.model.areas.keys():
    area = run.model.areas[key]
    if area.market_price_area != None and area.market_price_area.name in areas:
        storable_inflow = area.aggregated_hydro.storable_inflow(unit="GWh",time_axis=time_axis)
        non_storable_inflow = area.aggregated_hydro.nonstorable_inflow(unit="GWh", time_axis = time_axis)
        bypass = area.aggregated_hydro.bypass(unit="GWh", time_axis = time_axis)
        spill = area.aggregated_hydro.spillage(unit="GWh", time_axis=time_axis)
        energy_inflow += storable_inflow + non_storable_inflow - bypass - spill


df, pip = to_pandas(energy_inflow)
df = df.magnitude
df.columns = years + [df.columns[-1]]
df.to_csv("inflow_sweden.csv")