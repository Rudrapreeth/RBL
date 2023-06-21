import math
import matplotlib.pyplot as plt

def on_chip_waveform(frequency, amplitude, duration):
  """Calculates the on-chip waveform for a given frequency, amplitude, and duration.

  Args:
    frequency: The frequency in MHz.
    amplitude: The amplitude in volts.
    duration: The duration in seconds.

  Returns:
    A list of the on-chip waveform values.
  """

  waveform = []
  for i in range(int(duration * frequency)):
    value = amplitude * math.sin(2 * math.pi * frequency * i)
    waveform.append(value)

  return waveform

def main():
  """Prints the on-chip waveform for 50 MHz, 1 volt, and 1 second."""

  waveform = on_chip_waveform(50, 1, 1)
  plt.plot(waveform)
  plt.title("On-chip measured voltage waveforms of ECDSA engine at 50 MHz")
  plt.xlabel("Time (s)")
  plt.ylabel("Voltage (V)")
  plt.show()

if __name__ == "__main__":
  main()
