from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa

t0 = sa.utctime_now()

rr = RunRepository()

run_id = rr.find_closest_operational_run(t0)

run = rr.recreate(run_id = run_id)

print("Number of areas = " + str(len(run.model.areas)))