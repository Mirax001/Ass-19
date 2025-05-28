# Writing smart meter readings to a file
readings = [245.6, 238.1, 250.4, 243.0]

with open('smart_meter_data.txt', 'w') as file:
    for reading in readings:
        file.write(f"{reading}\n")

# Appending a new reading
with open('smart_meter_data.txt', 'a') as file:
    file.write("249.7\n")

# Reading entire file content
with open('smart_meter_data.txt', 'r') as file:
    all_content = file.read()
    print("File Content (read):")
    print(all_content)

# Reading file line by line
with open('smart_meter_data.txt', 'r') as file:
    lines = file.readlines()
    print("File Content (readlines):", lines)

# Reading individual lines using readline
with open('smart_meter_data.txt', 'r') as file:
    print("File Content (readline):")
    line = file.readline()
    while line:
        print(line.strip())  # remove trailing newline
        line = file.readline()