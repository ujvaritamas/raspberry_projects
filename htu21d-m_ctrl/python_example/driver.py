import smbus2
import time

# HTU21D I2C address
HTU21D_I2C_ADDR = 0x40

# Commands
CMD_MEASURE_TEMP_HOLD = 0xE3
CMD_MEASURE_HUMID_HOLD = 0xE5

# Function to read raw data from the sensor
def read_sensor(bus, command):
    bus.write_byte(HTU21D_I2C_ADDR, command)
    time.sleep(0.05)  # Wait for the measurement to complete
    data = bus.read_i2c_block_data(HTU21D_I2C_ADDR, 0, 3)
    return data

# Function to calculate temperature from raw data
def calculate_temperature(data):
    raw_temp = (data[0] << 8) | data[1]
    raw_temp &= 0xFFFC  # Clear the status bits
    temperature = -46.85 + (175.72 * raw_temp / 65536.0)
    return temperature

# Function to calculate humidity from raw data
def calculate_humidity(data):
    raw_hum = (data[0] << 8) | data[1]
    raw_hum &= 0xFFFC  # Clear the status bits
    humidity = -6.0 + (125.0 * raw_hum / 65536.0)
    return humidity

def main():
    # Initialize the I2C bus
    bus = smbus2.SMBus(1)

    try:
        while True:
            # Read temperature
            temp_data = read_sensor(bus, CMD_MEASURE_TEMP_HOLD)
            temperature = calculate_temperature(temp_data)
            print(f"Temperature: {temperature:.2f} °C")

            # Read humidity
            humid_data = read_sensor(bus, CMD_MEASURE_HUMID_HOLD)
            humidity = calculate_humidity(humid_data)
            print(f"Humidity: {humidity:.2f} %RH")

            # Wait before the next reading
            time.sleep(5)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
    finally:
        bus.close()

if __name__ == "__main__":
    main()
