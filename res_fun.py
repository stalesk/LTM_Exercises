from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
from statkraft.ltm.state import quantity

t0 = sa.utctime_now()
rr = RunRepository()
run_id = rr.find_closest_operational_run(t0, labels=['operational', 'norway', 'season'])

run = rr.recreate(run_id=run_id)
