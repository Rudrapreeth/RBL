import math
import matplotlib.pyplot as plt

def on_chip_lfi(frequency, amplitude, duration):
  """Calculates the on-chip LFI for a given frequency, amplitude, and duration.

  Args:
    frequency: The frequency in MHz.
    amplitude: The amplitude in volts.
    duration: The duration in seconds.

  Returns:
    A list of the on-chip LFI values.
  """

  lfi = []
  for i in range(int(duration * frequency)):
    value = amplitude * math.sin(2 * math.pi * frequency * i)
    lf = value * value / 4 * math.pi * frequency
    lfi.append(lf)

  return lfi

def main():
  """Prints the on-chip LFI for 50 MHz, 1 volt, and 1 second."""

  lfi = on_chip_lfi(50, 1, 1)
  plt.plot(lfi)
  plt.title("On-chip characterization of LFI")
  plt.xlabel("Time (s)")
  plt.ylabel("LFI (V^2/Hz)")
  plt.show()

if __name__ == "__main__":
  main()
