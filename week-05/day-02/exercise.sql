-- CREATE KEYSPACE isd_weather_data WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor' : 1};

-- source 'D:\EPAM\Data Scientist Academy\Eveosev\week-05\day-02\data\load-timeseries.cql';

-- COPY raw_weather_data (wsid, year, month, day, hour, temperature, dewpoint, pressure, wind_direction, wind_speed, sky_condition, one_hour_precip, six_hour_precip)
-- FROM 'D:\EPAM\Data Scientist Academy\Eveosev\week-05\day-02\data/2014.csv';


#exercise1
SELECT *
FROM weather_station
WHERE id = '724940:23234';

The weather station of id '724940:23234' is in US.
 id           | call_sign | country_code | elevation | lat    | long   | name                  | state_code
--------------+-----------+--------------+-----------+--------+--------+-----------------------+------------
 724940:23234 |      KSFO |           US |       2.4 | 37.617 | -122.4 | SAN FRANCISCO INTL AP |         CA


#exercise2
SELECT temperature
FROM raw_weather_data
WHERE wsid = '724940:23234' 
	AND year = 2008
	AND month = 6
	AND day = 1;

 temperature
-------------
          15
          15
        15.6
          15
          15
        14.4
        13.3
        12.2
        11.7
        10.6
          10
          10
        10.6
        11.1
        11.1
           0
        11.7
        11.7
        11.7
        11.7
        11.7
        12.2
        12.8
        13.3

(24 rows)

#exercise3
SELECT temperature
FROM raw_weather_data
WHERE wsid = '724940:23234' 
	AND year = 2008
	AND month = 6
	AND day = 1
    AND hour >= 9
    AND hour <= 15;

 temperature
-------------
        11.7
        10.6
          10
          10
        10.6
        11.1
        11.1

(7 rows)

#exercise4
SELECT AVG(elevation)
FROM weather_station
WHERE country_code = 'IN'
ALLOW FILTERING;

 system.avg(elevation)
-----------------------
             381.37572

(1 rows)

#exercise5
SELECT max(lat)
FROM weather_station
WHERE country_code = 'US'
    AND state_code = 'TX'
ALLOW FILTERING;

 system.max(lat)
-----------------
          36.017

(1 rows)

#exercise6
INSERT INTO raw_weather_data (wsid, year, month, day, hour, temperature) VALUES ('shenzhen', 2019, 6, 4, 18, 27);

#exercise7
SELECT wsid, year, month, day, hour, max(temperature) as high, min(temperature) as low, avg(temperature) as mean, sqrt(var(temperature)) as stdev, var(temperature) as var
FROM raw_weather_data
GROUP BY wsid, year, month, day, hour
ALLOW FILTERING;
