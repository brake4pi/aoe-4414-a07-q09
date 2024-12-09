# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
#  Determines the maximum possible bitrate
# Parameters:
#  tx_w: Transmitted Power in W
#  tx_gain_db: Transmitter gain in dB
#  freq_hz: Frequency in Hz
#  dist_km: Distance in Km
#  rx_gain:_db: 
#  n0_j: Noise Spectral Density
#  bw_hz: Channel Bandwidth
# Output:
#  A description of the script output
#
# Written by Lee Wallenfang
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math
# "constants"
#R_E_KM = 6378.137
transmitter_to_antenna_loss = 1 # dB
speed_of_light = 2.99792458e8 # m/s
atm_loss = 1 # dB
# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
tx_w = float('Nan')
tx_gain_db = float('Nan')
freq_hz = float('Nan')
dist_km = float('Nan')
rx_gain_db = float('Nan')
n0_j = float('Nan')
bw_hz = float('Nan')

# parse script arguments
if len(sys.argv)==8:
   tx_w = float(sys.argv[1])
   tx_gain_db = float(sys.argv[2])
   freq_hz = float(sys.argv[3])
   dist_km = float(sys.argv[4])
   rx_gain_db = float(sys.argv[5])
   n0_j = float(sys.argv[6])
   bw_hz = float(sys.argv[7])
else:
   print(\
    'Usage: '\
    'python3  max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
   )
   exit()

# write script below this line

# B: Bandwidth
# C: Signal Power over bandwidth
# N: Noise Power over bandwidth

B = bw_hz
N = n0_j*B
channel_wavelength = speed_of_light/freq_hz
dist_m = dist_km*1000
C = tx_w*transmitter_to_antenna_loss*tx_gain_db*((channel_wavelength/(4*math.pi*dist_m))**2)*atm_loss*rx_gain_db

r_max = B*math.log2(1+C/N)

print(math.floor(r_max))