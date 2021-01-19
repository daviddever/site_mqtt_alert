#! /usr/bin/env python3

import requests
import paho.mqtt.publish as mqtt
import yaml


def load_config(config_file_path):
    "Return a dictionary from yaml config file"
    with open(config_file_path) as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)

    return config


def check_site(site_address):
    "Request site and return status code"
    request = requests.get(site_address)

    return request.status_code


def mqtt_message(topic, message, host, port, client_id, username=None, password=None):
    "Send mqtt message"
    mqtt.single(
        topic, message, host, port, client_id, username, password, keepalive=60, qos=60
    )


full_config = load_config("./config/config.yaml")
mqtt_config = full_config["mqtt"]
sites = full_config["sites"]

for site in sites:
    site_code = check_site(site["address"])
    mqtt_message(
        site,
        site_code,
        mqtt_config["host"],
        mqtt_config["port"],
        mqtt_config["client_id"],
        mqtt_config["username"],
        mqtt_config["password"],
    )
