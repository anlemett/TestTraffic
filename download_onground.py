import os
#os.environ['http_proxy'] = "http://proxy.onera.fr:80"

DATA_DIR = os.path.join(".", "Data")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

import pickle

from traffic.data import airports, opensky

flights = opensky.history(

    "2022-08-01 06:00",
    "2022-08-01 18:00",
    bounds=airports["ESSA"],
    )


filename_full_data = os.path.join(DATA_DIR, "all_2022_08_01.csv")
filename_onground_data = os.path.join(DATA_DIR, "all_onground_2022_08_01.csv")
filename_onground_lat_lon = os.path.join(DATA_DIR, "all_lat_lon_2022_08_01.csv")

print(flights)

df = flights.data

df.to_csv(filename_full_data, sep=' ', encoding='utf-8', float_format='%.6f', header=True, index = False)

ground_flights = flights.query('onground | (altitude < 100)')

with open('traffic_object_2022_08_01', 'wb') as traffic_object_file:
 
  pickle.dump(ground_flights, traffic_object_file)

ground_df = ground_flights.data

ground_df = ground_df[ground_df['callsign'].notna()]

ground_df.to_csv(filename_onground_data, sep=' ', encoding='utf-8', float_format='%.6f', header=True, index = False)

ground_df = ground_df[["callsign", "latitude", "longitude"]]

ground_df.to_csv(filename_onground_lat_lon, sep=' ', encoding='utf-8', float_format='%.6f', header=True, index = False)

