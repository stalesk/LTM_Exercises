from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa

t0 = sa.utctime_now()

rr = RunRepository()
run_id = rr.find_closest_operational_run(t0)
run = rr.recreate(run_id = run_id)

max_steps = -9999
the_area = None

for area in run.model.areas:
    objArea = run.model.areas[area]
    if len(objArea.consumption) > max_steps:
        the_area = area
        max_steps = len(objArea.consumption)

print(the_area)
print(max_steps)