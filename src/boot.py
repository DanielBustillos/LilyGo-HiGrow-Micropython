from main_utils import open_text_file

print("Reading config files")

# Read config files
device_config = open_text_file("./device_config.txt", json=True)
blynk_config = open_text_file("./blynk_config.txt", json=True)

# Define device pins
pin_dht = device_config["pin_dht"]
pin_battery = device_config["pin_battery"]
pin_light_sensor_scl = device_config["pin_light_sensor_scl"]
pin_light_sensor_sda = device_config["pin_light_sensor_sda"]
pin_salt_sensor = device_config["pin_salt_sensor"]
pin_moisture = device_config["pin_moisture"]

# Define Blynk variables
blynk_token = device_config["blynk_token"]
debug_state = device_config["debug_state"]
time_deepsleep_minutes = device_config["time_deepsleep_minutes"]

