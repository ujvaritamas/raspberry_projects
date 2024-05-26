import subprocess
import re

# Call the C++ program and capture its output
output = subprocess.check_output(["../cpp_example/get_sensor_data"])

temperature_pattern = r"Temperature: (\d+\.\d+)C"
humidity_pattern = r"Humidity: (\d+\.\d+)C"


# Split the output into lines and print each line
for line in output.splitlines():
    decoded_line = line.decode()

    match = re.search(temperature_pattern, decoded_line)

    if match:
        temperature = float(match.group(1))
        print("Temperature:", temperature)
    else:
        print("Temperature not found in the output.")

    match = re.search(humidity_pattern, decoded_line)

    if match:
        humidity = float(match.group(1))
        print("Humidity:", humidity)
    else:
        print("Humidity not found in the output.")
