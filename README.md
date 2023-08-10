# InfluxDB 3.0 Quick Starts
Welcome to the "InfluxDB IOx Quick Starts" repository! This repository is dedicated to providing easy to follow tutorials on how to integrate InfluxDB IOx with Grafana and Superset. InfluxDB IOx is a powerful time-series database solution and when paired with Grafana or Superset, both popular open-source visualization platform, you can create beautiful and informative dashboards to better visualize and understand your data.

This repository will cover the basics of setting up InfluxDB IOx and Grafana or Superset, how to connect them and how to query data from InfluxDB IOx. Whether you are new to InfluxDB IOx or an experienced user, this repository is designed to help you get up and running with InfluxDB IOx, Grafana and Superset quickly and easily.

# Grafana

## Setup
Please make sure you have the following prerequisites before you begin:
- [Docker](https://docs.docker.com/get-docker/)
- [InfluxDB IOx](https://github.com/InfluxCommunity/InfluxDB-IOx-Quick-Starts#influxdb-iox)
- [Env file](https://github.com/InfluxCommunity/InfluxDB-IOx-Quick-Starts#env-file)
- [Grafana flighsql plugin](https://github.com/InfluxCommunity/InfluxDB-IOx-Quick-Starts#grafana-flighsql-plugin)

### InfluxDB IOx
To get started, you will need to create an InfluxDB IOx account. If you don't already have an account, you can sign up for free [here](https://cloud2.influxdata.com/signup). Once you have an account, you can create a new organization and bucket to store your data. You can find instructions on how to do this [here](https://docs.influxdata.com/influxdb/cloud/organizations/buckets/create-bucket/).

### Env file
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
**Note: make sure to specify your `INFLUX_HOST` without the protocal like so: `us-east-1-1.aws.cloud2.influxdata.com`**

## Run
To run a quick start, make sure to first source the env file:
```bash
source .env
```
Navigate to the quick start you would like to run and run the following command:
```bash
docker-compose -f system-monitoring/docker-compose.yml up -d
```
This will start Grafana server and Telegraf. Once the quick start is running, you can access Grafana at `localhost:3000`. You can log in with the default username and password: `admin` and `admin`.
