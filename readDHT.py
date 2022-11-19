import os, sys, time
import sqlite3
from datetime import datetime

sensor = 11
pin = 4

try:
	#����������� � ��
	db = sqlite3.connect('sensorData.db')
	sql = db.cursor()
	sql.execute("""CREATE TABLE IF NOT EXISTS sensorReading (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	readingTime DATE,
	temperature REAL,
	humidity REAL	
	)""")
	db.commit()

	#������ ��������� �������
	nowtime = datetime.now()
	attemptCount = 0
	while True:
		humidity, temperature = None, None
		if (humidity is not None) and (temperature is not None):
			#���������� ��������� �������
			sql.execute("""INSERT INTO sensorReading (readingTime, temperature, humidity) VALUES (?, ?, ?);""", (nowtime, 25, 50))
			db.commit()
			break
		if attemptCount >= 10:	 #����� ������ ������� �� �������
			#�������� ������ ������
			sql.execute("""INSERT INTO sensorReading (readingTime, temperature, humidity) VALUES (?, ?, ?);""", (nowtime, None, None))
			db.commit()
			break
		attemptCount += 1
	sql.close()
except Exception as ex:
	print("Error:")
	print(ex)	
finally:
	db.close()
