# (c) stona@gmail.com
# example of using average filter from simple filters library
# visualise filtered data using matplotlib library



import filters
import matplotlib.pyplot as plt

# import example preset data samples from data.py file
import data
# choose one data set from below
#dane = data.sinus
dane = data.data

# create empty arrays for filtered data
dane_average_2 = []
dane_average_4 = []
dane_average_8 = []
dane_average_16 = []

# create a filtered data arrays with vary filters parameter
filters.filter.average_filter_reset(2)
for i in range (len(dane)):
  dane_average_2.append( filters.filter.average_filter(dane[i]) )

filters.filter.average_filter_reset(4)
for i in range (len(dane)):
  dane_average_4.append( filters.filter.average_filter(dane[i]) )

filters.filter.average_filter_reset(8)
for i in range (len(dane)):
  dane_average_8.append( filters.filter.average_filter(dane[i]) )

filters.filter.average_filter_reset(16)
for i in range (len(dane)):
  dane_average_16.append( filters.filter.average_filter(dane[i]) )

# plot all data on graph
plt.plot( range(len(dane)), dane ,label='input')
plt.plot( range(len(dane)), dane_average_2, label='2 samples')
plt.plot( range(len(dane)), dane_average_4, label='4 samples')
plt.plot( range(len(dane)), dane_average_8, label='8 samples')
plt.plot( range(len(dane)), dane_average_16, label='16 samples')

plt.legend()
plt.show()
