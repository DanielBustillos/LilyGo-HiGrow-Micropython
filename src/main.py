import time
import sensors_utils as SensorsUtils
import network_utils as network_utils
from machine import Pin, deepsleep


print("Starting measurement")

# Measure sensors
p0 = Pin(4, Pin.OUT)  # Set pin 4 to high state to measure pin states
p0.value(1)  # Set pin to high/on

# Battery
battery_reading = SensorsUtils.battery_sampling_function(
    pin_number=pin_battery,
    sample_size=15,
    inter_time=0.2,
    include_raw=True
)

# DHT temperature and humidity
temp_air_1, hum_air_1 = SensorsUtils.temp_hum_air(pin_dht)

# Soil moisture
soil_moist, soil_moist_raw = SensorsUtils.capacity_sampling_function(
    pin_number=pin_moisture,
    sample_size=15,
    inter_time=0.2,
    include_raw=True
)

# Salt sensor
salt_value = SensorsUtils.salt_sensor_sampler(
    salt_pin=pin_salt_sensor,
    max_value=4095,
    min_value=0,
    n_sample=3,
    time_samples=0.5
)

# Light sensor
light_measurement = SensorsUtils.light_sensor_bh1750(
    pin_light_sensor_scl,
    pin_light_sensor_sda
)

# Set pin 4 to low state
p0.value(0)  # Set pin to low/off

data_dict = {
    'Battery_level': battery_reading,
    'Temperature_air': temp_air_1,
    'Humidity_air': hum_air_1,
    'Fertility': salt_value,
    'Soil_moisture': soil_moist,
    'light_level': light_measurement,
    'salt_value': salt_value
}

print(data_dict)


# Sending data to Blynk
print("Sending data to Blynk\n")

# Connect to Wi-Fi network
network_utils.do_connect(SSID=device_config["SSID"], PASSWORD=device_config["PASSWORD"])

# Send data
for element, value in data_dict.items():
    network_utils.get_request(
        device_token=blynk_token,
        pin_name=blynk_config[element],
        value_to_post=round(value, 1),
        debug=debug_state
    )


# Deepsleep
print("Starting Deepsleep")
deepsleep(int(time_deepsleep_minutes * 60 * 1000))  # Convert minutes to ms
