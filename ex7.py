from statkraft.ltm.io.run_repository import RunRepository
import shyft.api as sa
from statkraft.ltm.state import quantity
from statkraft.ltm.scripting import plot_ts
import matplotlib.pyplot as plt

rr = RunRepository()
t0 = sa.utctime_now()
run_id = rr.find_closest_operational_run(t0)

run = rr.recreate(run_id = run_id)
calendar = sa.Calendar("Europe/Oslo")
dt = 3 * calendar.HOUR
n = calendar.diff_units(run.time_axis.total_period().start, run.time_axis.total_period().end, dt)
time_axis = sa.TimeAxis(run.start_utc, dt,n)
norway = run.model.countries['Norway']
tsv = quantity(sa.TsVector(), "EUR")

legend_list = []

#val_in_eur = quantity(sa.TsVector(), "EUR")
values = None

for m_area in norway.aggregation_list:
    price = m_area.power_price(time_axis=time_axis, unit = "EUR/MWh")
    production = m_area.production(time_axis=time_axis, unit = "MWh")
    val_in_eur =  price * production
    if values is None:
        values = val_in_eur
    else:
        values += val_in_eur

#values_percentiles = quantity(values.percentiles(time_axis=time_axis),unit="EUR")

"""
m_area = norway.aggregation_list[1]
price = m_area.power_price.percentiles(time_axis=time_axis,unit="EUR/MWh")
prod = m_area.production.percentiles(time_axis=time_axis,unit="MWh")
val_in_eur = price * prod
legend_list.append(m_area.name)
"""

plot_ts(values.percentiles(time_axis=time_axis))
plt.legend(["Norway prod value"])
plt.show(block=True)