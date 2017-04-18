1. Install Mongodb and start mongod
2. Execute "mongoimport --db quartet --collection quartetClinics --drop --file /path/to/repo/QuartetAssignment/quartetCollection.json --jsonArray" to insert data to be matched against.
3. python ./dataPlatformExercise.py  for Test Run
3. Following steps to setup the cron job for the py script to run every day at midnight:
    user> crontab -e
    Append "00 00 * * * /path/to/repo/QuartetAssignment/bin/dataPlatformExercise.py"
    Save & Exit
