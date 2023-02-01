# InfluxDB IOx Quick Starts
Welcome to the "InfluxDB IOx Quick Starts" repository! This repository is dedicated to providing easy to follow tutorials on how to integrate InfluxDB IOx with Grafana. InfluxDB IOx is a powerful time-series database solution and when paired with Grafana, a popular open-source visualization platform, you can create beautiful and informative dashboards to better visualize and understand your data.

This repository will cover the basics of setting up InfluxDB IOx and Grafana, how to connect them and how to query data from InfluxDB IOx in Grafana. Whether you are new to InfluxDB IOx or an experienced user, this repository is designed to help you get up and running with InfluxDB IOx and Grafana quickly and easily.

So, if you're ready to dive into the world of time-series data visualization with InfluxDB IOx and Grafana, let's get started!

## Setup
Please make sure you have the following prerequisites before you begin:
- [Docker](https://docs.docker.com/get-docker/)
- [InfluxDB IOx]()
- [Env file]()
- [Grafana flighsql plugin]()

# InfluxDB IOx
To get started, you will need to create an InfluxDB IOx account. If you don't already have an account, you can sign up for free [here](https://cloud2.influxdata.com/signup). Once you have an account, you can create a new organization and bucket to store your data. You can find instructions on how to do this [here](https://docs.influxdata.com/influxdb/cloud/organizations/buckets/create-bucket/).

# Env file
To connect Grafana to InfluxDB IOx, you will need to create an env file. With the top directory create a file called `.env`:
```bash
touch .env
```
This file will contain the following information:
```
export INFLUX_HOST=
export INFLUX_TOKEN=
export INFLUX_ORG=
export INFLUX_BUCKET=
```
# Grafana flighsql plugin
To connect Grafana to InfluxDB IOx, you will need to install the Grafana flighsql plugin. To do this follow these instructions [here](https://docs.influxdata.com/influxdb/cloud-iox/visualize-data/grafana/).

Once you have downloaded the plugin, unzip the folder and copy the `influxdata-flightsql-datasource` directory to the `plugins` directory in the top directory of this repository.

## Run
To run a quick start, make sure to first source the env file:
```bash
source .env
```
Navigate to the quick start you would like to run and run the following command:
```bash
docker-compose up -d
```
This will start Grafana server and Telegraf. Once the quick start is running, you can access Grafana at `localhost:3000`. You can log in with the default username and password: `admin` and `admin`.