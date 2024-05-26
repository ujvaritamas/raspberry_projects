import smbus2
import time

# HTU21D I2C address
HTU21D_I2C_ADDR = 0x40

# Commands
REG_TEMP = 0xE3
REG_HUM = 0xE5

# Function to get temperature
def get_temperature(bus):
    # Send temperature measurement command
    bus.write_byte(HTU21D_I2C_ADDR, REG_TEMP)
    time.sleep(0.1)  # Wait for measurement to complete
    # Read 3 bytes of data
    data = bus.read_i2c_block_data(HTU21D_I2C_ADDR, 0, 3)
    # Convert sensor reading into temperature
    temp = (data[0] << 8 | data[1]) & 0xFFFC
    t_sensor_temp = temp / 65536.0
    return -46.85 + (175.72 * t_sensor_temp)

# Function to get humidity
def get_humidity(bus):
    # Send humidity measurement command
    bus.write_byte(HTU21D_I2C_ADDR, REG_HUM)
    time.sleep(0.1)  # Wait for measurement to complete
    # Read 3 bytes of data
    data = bus.read_i2c_block_data(HTU21D_I2C_ADDR, 0, 3)
    # Convert sensor reading into humidity
    humid = (data[0] << 8 | data[1]) & 0xFFFC
    t_sensor_humid = humid / 65536.0
    return -6.0 + (125.0 * t_sensor_humid)

def main():
    # Open I2C bus
    bus = smbus2.SMBus(1)  # 1 indicates /dev/i2c-1

    while True:
        # Read temperature and humidity
        temperature = get_temperature(bus)
        humidity = get_humidity(bus)
        # Print temperature and humidity
        print(f"{temperature:.2f}°C")
        print(f"{humidity:.2f}%RH")
        # Delay for 5 seconds before next reading
        time.sleep(5)

if __name__ == "__main__":
    main()
