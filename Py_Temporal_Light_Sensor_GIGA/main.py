import serial
import temporal_light_sensor
import matplotlib.pyplot as plt
import numpy as np

def main():
    sensor = temporal_light_sensor.TemporalLightSensor(serial.Serial("COM5", 500000))

    sampling_frequency = 5000
    sensor.take_measurement(num_measurements=50000, sampling_frequency=sampling_frequency)

    measurements, start_ts = sensor.get_results()

    plt.plot(np.arange(len(measurements)) * 1/sampling_frequency, measurements / 65535)
    plt.ylim((0, 1))
    plt.show()


if __name__ == "__main__":
    main()
