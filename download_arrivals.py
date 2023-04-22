import os

DATA_DIR = os.path.join(".", "Data")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
    
from traffic.data import opensky

flights = opensky.history(

        start="2022-09-01 00:00",

        stop="2022-10-01 00:00",

        arrival_airport="ESSA",
        #departure_airport="ESSA",

        serials=(-1408232560, -1408232534),

    )


filename_full_data = os.path.join(DATA_DIR, "arrivals_2022_09_01.csv")

print(flights)

#print(flights.data.head())

df = flights.data

df.to_csv(filename_full_data, sep=' ', encoding='utf-8', float_format='%.6f', header=True, index = False)

df = df.set_index("callsign")
print(len(df.groupby(level="callsign")))
