import os
import psycopg2
from dataqualitychecks import check_for_nulls
from dataqualitychecks import check_for_min_max
from dataqualitychecks import check_for_valid_values
from dataqualitychecks import check_for_duplicates
from dataqualitychecks import run_data_quality_check


pgpassword = os.environ.get('POSTGRES_PASSWORD')
conn = None
try:
	conn = psycopg2.connect(
		user = "postgres",
	    password = pgpassword,
	    host = "localhost",
	    port = "5432",
	    database = "postgres")
except Exception as e:
	print("Error connecting to data warehouse")
	print(e)
else:
	print("Successfully connected to warehouse")
finally:
	if conn:
		conn.close()
		print("Connection closed")

#start of data quality checks
results = []
tests = {key:value for key,value in mytests.__dict__.items() if key.startswith('test')}
for testname,test in tests.items():
	test['conn'] = conn
	results.append(run_data_quality_check(**test))
	