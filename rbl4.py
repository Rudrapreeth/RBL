import math
import random
import matplotlib.pyplot as plt

def measured_substrate_voltage_waveforms(frequency, amplitude, duration):
  """Calculates the measured substrate voltage waveforms for a given frequency, amplitude, and duration.

  Args:
    frequency: The frequency in MHz.
    amplitude: The amplitude in volts.
    duration: The duration in seconds.

  Returns:
    A list of the measured substrate voltage waveforms.
  """

  waveforms = []
  for i in range(int(duration * frequency)):
    value = amplitude * math.sin(2 * math.pi * frequency * i) + random.random() * 0.1
    waveforms.append(value)

  return waveforms

def main():
  """Prints the measured substrate voltage waveforms for 50 MHz, 1 volt, and 1 second."""

  waveforms = measured_substrate_voltage_waveforms(50, 1, 1)
  plt.plot(waveforms)
  plt.title("Measured substrate voltage waveforms in laser irradiation")
  plt.xlabel("Time (s)")
  plt.ylabel("Voltage (V)")
  plt.show()

if __name__ == "__main__":
  main()
