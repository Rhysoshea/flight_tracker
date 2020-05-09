import urllib.request
import json
import sqlite3
import pandas as pd

def updatesql(data):
##    data = data[:10]

    conn = sqlite3.connect('aircraft.db')
    
    c = conn.cursor()
##    c.execute("select schema from sqlite_master where type = 'table';")
##    print(c.fetchall())
##    exit()
    
    
    icao = data[0]
    callsign = data[1]
    origin_country = data[2]
    time_position = data[3]
    last_contact = data[4]
    longitude = data[5]
    latitude = data[6]
    altitude = data[7]
    on_ground = data[8]
    velocity = data[9]
    true_track = data[10]
    c.execute("INSERT INTO live(icao24,callsign,origin_country,time_position,last_contact,longitude,latitude,altitude,on_ground,velocity,true_track)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(icao,callsign,origin_country,time_position,last_contact,longitude,latitude,altitude,on_ground,velocity,true_track))
    conn.commit()
    conn.close()
    print("Success")

def fetchall():
    response = urllib.request.urlopen("http://opensky-network.org/api/states/all")
    html = response.read().decode("utf8")
    json_data = json.loads(html)

    for entry in json_data["states"]:
        print(entry)
        updatesql(entry)

def check():
    db = sqlite3.connect('aircraft.db')
    table = pd.read_sql_query("select * from live", db)
    table.to_csv("live.csv")
    
if __name__ == "__main__":
##    fetchall()
    check()
    