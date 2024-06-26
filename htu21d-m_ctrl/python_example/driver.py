import subprocess
import re

# Call the C++ program and capture its output
output = subprocess.check_output(["../cpp_example/get_sensor_data"])

temperature_pattern = r"Temperature: (\d+\.\d+)C"
humidity_pattern = r"Humidity: (\d+\.\d+)%rh"


# Split the output into lines and print each line
for line in output.splitlines():
    decoded_line = line.decode()

    matchT = re.search(temperature_pattern, decoded_line)

    if matchT:
        temperature = float(matchT.group(1))
        print("Temperature:", temperature)
        continue

    matchH = re.search(humidity_pattern, decoded_line)

    if matchH:
        humidity = float(matchH.group(1))
        print("Humidity:", humidity)
        continue
