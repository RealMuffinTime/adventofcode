# Advent of code 2022 day 15 have fun.
# https://adventofcode.com/2022/day/15

def run(file_name, field):
    sensors = []

    with open(file_name) as file:
        for line in file.readlines():
            line.strip()
            sensor, beacon = line.strip("Sensor at x=").replace("y=", "").split(": closest beacon is at x=")
            sensor_x, sensor_y = [int(i) for i in sensor.split(", ")]
            beacon_x, beacon_y = [int(i) for i in beacon.split(", ")]
            sensors.append([sensor_x, sensor_y, beacon_x, beacon_y])

    # Haha, even more exhausting
    for y in range(field):
        positions = []
        for sensor in sensors:
            distance_y = sensor[1] - sensor[3]
            distance_x = sensor[0] - sensor[2]
            reach = abs(distance_x) + abs(distance_y)
            if sensor[1] <= y <= sensor[1] + reach or sensor[1] >= y >= sensor[1] + reach or sensor[1] >= y >= sensor[1] - reach or sensor[1] <= y <= sensor[1] - reach:
                y1 = abs(sensor[1] - y)
                x1 = abs(reach - y1) + sensor[0]
                x2 = abs(reach - y1) * -1 + sensor[0]

                position = [x1, x2]
                position.sort()
                if position[0] < 0:
                    position[0] = 0
                if position[1] > field:
                    position[1] = field
                positions.append(position)

        positions.sort()
        i = 0
        while i < len(positions) - 1:
            if positions[i + 1][1] >= positions[i][1] >= positions[i + 1][0]:
                positions[i][1] = positions[i + 1][1]
                del positions[i + 1]
                i = 0
            elif positions[i][1] >= positions[i + 1][1]:
                del positions[i + 1]
                i = 0
            elif positions[i][1] + 1 == positions[i + 1][0]:
                positions[i][1] = positions[i + 1][1]
                del positions[i + 1]
                i = 0
            elif positions[i][1] <= positions[i + 1][0]:
                i += 1

        if positions[0][0] != 0:
            print(f"Distress beacon at {[0, y]}")
            print(f"Tuning frequency: {0 * 4000000 + y}")
        elif positions[-1][1] != field:
            print(f"Distress beacon at {[field, y]}")
            print(f"Tuning frequency: {field * 4000000 + y}")
        elif len(positions) == 2:
            print(f"Distress beacon at {[positions[0][1] + 1, y]}")
            print(f"Tuning frequency: {(positions[0][1] + 1) * 4000000 + y}")

run("input15_", field=20)
run("input15", field=4000000)
