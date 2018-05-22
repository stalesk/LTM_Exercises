from statkraft.ltm.io.run_repository import RunRepository
from statkraft.ltm.scripting import plot_ts, plot_percentiles
import matplotlib.pyplot as plt

rr = RunRepository()
labels = ["operational", "daily", "samtap sk"]
run_id = sorted(rr.search(labels=labels))[-1] # Pick newest
run = rr.recreate(run_id=run_id)

no1 = run.model.market.areas["NO1"] # shortcut variable
st1 = no1.power_price
mean = st1.mean()
plot_percentiles(no1.power_price.percentiles())
plt.figure()
plot_ts(no1.power_price.mean())

plt.show()
m = st1.mean
print(m)