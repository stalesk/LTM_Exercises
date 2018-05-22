from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
from statkraft.ltm.state import quantity
from statkraft.ltm.scripting import plot_ts
from statkraft.ltm.domain_model.detailed_hydro import PowerStation
rr = RunRepository()
t0 = sa.utctime_now()
run_id = rr.find_closest_operational_run(t0)

run = rr.recreate(run_id=run_id)

sorland = run.model.areas["Sorland"]
blasjo = sorland.detailed_hydro.reservoirs['16606']
stations = dict()

def findStation(ds):
    for obj in ds:
        if isinstance(obj,PowerStation):
            if not obj.local_tag in stations.keys():
                stations[obj.local_tag] = obj
        if obj is not None:
            findStation(obj.ds)

findStation(blasjo.ds)

print(stations)