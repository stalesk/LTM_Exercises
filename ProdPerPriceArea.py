from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
from statkraft.ltm.state import quantity

t0 = sa.utctime_now()
labels = ["norway", "operational", "season"]

rr = RunRepository()
run_id = rr.find_closest_operational_run(t=t0,labels=labels)

run = rr.recreate(run_id=run_id)

time_axis = run.fine_time_axis
min_share = 0.01
prod_price_area = {}
for key, val in run.model.market.areas.items():
    for m_area in val.aggregation_list:
        prod = quantity(0, "GWh")
        m_area_hyd = m_area.detailed_hydro
        if not m_area_hyd is None:
            for pws in m_area_hyd.power_stations.values():
                if pws.statkraft_share > min_share:
                    print(pws)
                    prod += pws.production.mean(time_axis = time_axis, unit="GWh")


