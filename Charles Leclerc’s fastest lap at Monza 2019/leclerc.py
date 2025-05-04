from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting

fastf1.plotting.setup_mpl(misc_mpl_mods=False, color_scheme='fastf1')

session = fastf1.get_session(2019, 'Monza', 'R')

session.load()
fast_leclerc = session.laps.pick_drivers('LEC').pick_fastest()
lec_car_data = fast_leclerc.get_car_data()
t = lec_car_data['Time']
vCar = lec_car_data['Speed']

# Plotting
fig, ax = plt.subplots()
t_seconds = t.dt.total_seconds()
ax.plot(t_seconds, vCar, label='Fast')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Leclerc - Fastest Lap Speed at Monza 2019')
ax.legend(['Leclerc Fastest Lap'])
plt.show()