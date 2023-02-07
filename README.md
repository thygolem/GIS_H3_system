## The system get data from 10sample.csv using csv_transform that help us order data and add cartesian coordinates to the daataframe

## Must install docker desktop and docker-compose in order to run the REDIS databse container
- docker-compose up -d

## Run redis_write.py to write data to the REDIS database

## Run redis_udp.py to read data from the REDIS database and send data through UDP to touchdesigner