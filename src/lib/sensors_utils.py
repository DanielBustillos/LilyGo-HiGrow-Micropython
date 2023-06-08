from machine import Pin, ADC, I2C
import dht
from utime import sleep_ms
from time import sleep

class BH1750:
    """
    Micropython BH1750 ambient light sensor driver.
    Complete project details at https://RandomNerdTutorials.com
    randomnerdtutorials.com/esp32-esp8266-dht11-dht22-micropython-temperature-humidity-sensor/
    """

    PWR_OFF = 0x00
    PWR_ON = 0x01
    RESET = 0x07

    # modes
    CONT_LOWRES = 0x13
    CONT_HIRES_1 = 0x10
    CONT_HIRES_2 = 0x11
    ONCE_HIRES_1 = 0x20
    ONCE_HIRES_2 = 0x21
    ONCE_LOWRES = 0x23

    # default addr=0x23 if addr pin floating or pulled to ground
    # addr=0x5c if addr pin pulled high
    def __init__(self, bus, addr=0x23):
        self.bus = bus
        self.addr = addr
        self.off()
        self.reset()

    def off(self):
        """Turn sensor off."""
        self.set_mode(self.PWR_OFF)

    def on(self):
        """Turn sensor on."""
        self.set_mode(self.PWR_ON)

    def reset(self):
        """Reset sensor, turn on first if required."""
        self.on()
        self.set_mode(self.RESET)

    def set_mode(self, mode):
        """Set sensor mode."""
        self.mode = mode
        self.bus.writeto(self.addr, bytes([self.mode]))

    def luminance(self, mode):
        """Sample luminance (in lux), using specified sensor mode."""
        # continuous modes
        if mode & 0x10 and mode != self.mode:
            self.set_mode(mode)
        # one shot modes
        if mode & 0x20:
            self.set_mode(mode)
        # earlier measurements return previous reading
        sleep_ms(24 if mode in (0x13, 0x23) else 180)
        data = self.bus.readfrom(self.addr, 2)
        factor = 2.0 if mode in (0x11, 0x21) else 1.0
        result = (data[0] << 8 | data[1]) / (1.2 * factor)
        return result


def light_sensor_bh1750(light_sensor_scl, light_sensor_sda):
    """
    Light sensor measurement using BH1750.
    :param light_sensor_scl: SCL pin number
    :param light_sensor_sda: SDA pin number
    :return: Light measurement in lux
    """
    i2c = I2C(1, scl=Pin(light_sensor_scl), sda=Pin(light_sensor_sda))
    light_sensor = BH1750(i2c)
    light_measurement = light_sensor.luminance(BH1750.ONCE_HIRES_1)
    return light_measurement


def battery_reader(battery_dtc, vref=1100):
    """
    Function to read battery voltage.
    :param battery_dtc: Battery DTC pin number
    :param vref: Voltage reference
    :return: Battery voltage
    """
    pin_number = int(battery_dtc)
    battery_level = ADC(Pin(pin_number))
    battery_level.atten(ADC.ATTN_11DB)
    battery_read = battery_level.read()

    val_voltage = (battery_read / 4095.0) * 6.6 * vref
    val_voltage = val_voltage / 291.8

    if val_voltage > 1:
        val_voltage = 100
    elif val_voltage < 1:
        val_voltage = val_voltage

    return val_voltage


def battery_sampling_function(pin_number, sample_size, inter_time, include_raw=True):
    """
    Function to sample battery voltage.
    :param pin_number: Battery pin number
    :param sample_size: Number of samples
    :param inter_time: Interval time between samples
    :param include_raw: Include raw values in the average
    :return: Average battery voltage
    """
    suma_valores = 0
    suma = 0
    suma_raw = 0
    if include_raw is True:
        for sample in range(sample_size):
            readed_value = battery_reader(battery_dtc=pin_number)
            suma_raw = suma_raw + readed_value
            promedio_raw = suma_raw / sample_size
            sleep(inter_time)

        return promedio_raw

    return promedio_raw


def temp_hum_air(pin_number):
    """
    Function to read temperature and humidity from DHT22 sensor.
    :param pin_number: DHT22 sensor pin number
    :return: Temperature and humidity values
    """
    sensor = dht.DHT11(Pin(pin_number))

    try:
        sleep(.2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        return temp, hum

    except Exception as e:
        log_originator = "./sensor_utils temp_hum_air"
        print('\n Exception: ', str(e))
        logger_info(origin=log_originator, message=e)
        sleep(3)
        reset()


def capacitance_soil_moisture(pin_number, water_value=1383, air_value=3520):
    """
    Function to read soil moisture with a capacitance sensor.
    :param pin_number: Soil moisture sensor pin number
    :param water_value: Value at water
    :param air_value: Value at air
    :return: Normalized soil moisture value and raw reading
    """
    pin_number = int(pin_number)
    soil = ADC(Pin(pin_number))
    soil.atten(ADC.ATTN_11DB)
    soil_read = soil.read()
    moisture = 100 - (100 * (soil_read - water_value) / (air_value - water_value))

    if moisture > 100:
        moisture = 100
    elif moisture < 0:
        moisture = 0

    return moisture, soil_read


def capacity_sampling_function(pin_number, sample_size, inter_time, include_raw):
    """
    Function to sample soil moisture with a capacitance sensor.
    :param pin_number: Soil moisture sensor pin number
    :param sample_size: Number of samples
    :param inter_time: Interval time between samples
    :param include_raw: Include raw values in the average
    :return: Average soil moisture and average raw reading
    """
    suma_valores = 0
    suma = 0
    suma_raw = 0
    if include_raw is True:
        for sample in range(sample_size):
            readed_value = capacitance_soil_moisture(pin_number=pin_number)
            suma_raw = suma_raw + readed_value[1]
            promedio_raw = suma_raw / sample_size

            suma = suma + readed_value[0]
            promedio = suma / sample_size
            sleep(inter_time)

        return promedio, promedio_raw

    for sample in range(sample_size):
        suma = suma + capacitance_soil_moisture(pin_number=pin_number)[0]
        promedio = suma / sample_size
        sleep(inter_time)

    return promedio_raw, promedio


def salt_sensor_sampler(salt_pin, n_sample, time_samples, min_value=0, max_value=0):
    """
    Function to read salt with a capacitance sensor.
    :param salt_pin: Salt sensor pin number
    :param n_sample: Number of samples
    :param time_samples: Interval time between samples
    :param min_value: Minimum value
    :param max_value: Maximum value
    :return: Normalized salt value
    """
    pot = ADC(Pin(salt_pin))
    suma_samples = 0
    for read in range(n_sample):
        pot_value = pot.read()
        suma_samples = pot_value + suma_samples
        sleep(time_samples)

    sampled_reading = suma_samples / n_sample
    salt_norm = (100 * (sampled_reading - min_value) / (max_value - min_value))

    if salt_norm > 100:
        salt_norm = 100
    elif salt_norm < 0:
        salt_norm = 0

    return salt_norm
