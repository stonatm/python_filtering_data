# (c) stonatm@gmail.com
# example of use simple python filter library
# average, EWMA and IIR filter

import filters
import matplotlib.pyplot as plt

# copy below link with your blynk api key and pin name into browser address
# http://blynk-cloud.com/YOUR_BLYNK_API_KEY/data/PIN_NAME
# and save downloaded gz compressed file from blynk to disk.
# unpack it and rename to data.csv

# parse data file from blynk pin history
dane = []
with open('./data.csv') as f:
  lines = f.readlines()
for i in range(len(lines)):
  dane.append( float(lines[i][0:lines[i].find(',',0)]) )

# initialize filtered data table
dane_average = []
dane_iir = []
dane_ewma = []

# initialize filters parameters
filters.filter.ewma_filter_reset(0.15)
filters.filter.iir_filter_reset(32)
filters.filter.average_filter_reset(16)

# calculate filtered data
for i in range (len(dane)):
  dane_ewma.append( filters.filter.ewma_filter(dane[i]) )
  dane_iir.append( filters.filter.iir_filter(dane[i]) )
  dane_average.append( filters.filter.average_filter(dane[i]) )

# plot all data with matplotlib library
plt.plot( range(len(dane)), dane ,label='input')
plt.plot( range(len(dane)), dane_ewma, label='ewma')
plt.plot( range(len(dane)), dane_iir, label='iir')
plt.plot( range(len(dane)), dane_average, label='average')

plt.legend()
plt.show()
