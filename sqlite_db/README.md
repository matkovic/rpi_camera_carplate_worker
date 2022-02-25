# Sqlite web browser

Browse SQLite database through browser: https://github.com/coleifer/sqlite-web

Install sqlite-web in environment (tflite1-env in this case)
```
source activate ~/tflite1/tflite1-env/bin/activate

sqlite_web /var/www/imgs/plates.db --port 8081 --read-only --host 0.0.0.0 --no-browser
```

Available on ```http://localhost:8081```

## Run flask app on startup as daemon

Create service file - content [sqlite_carplates.service](sqlite_carplates.service) in:
```
/etc/systemd/system/sqlite_carplates.service
```

Start service 
```
systemctl start sqlite_carplates.service
```

Enable on startup
```
systemctl enable mydaemon.service 
```