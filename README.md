# A simple filter library written in micro python for use in microcontrollers like esp8266, esp32.

The [filters.py](filters.py) library contains three types of filters:
- Average filter
- EWMA filter
- IIR filter

## Usage
Model of operation of filter functions: the first call to the **NAME_filter** function returns the value given as the input parameter **input**.
This value is also stored for the next calculations for the next calls of this function.
Next calls of this function continue calculations for **input** data for previously set filter parameters or defaults values (if parameters are not set).
Using the **NAME_filter_reset** function returns this state to the beginning.

### example code
```
# import library
import filters
# create sample input data table
input_data = [1, 2, 1, 4, 3, 4, 5, 2, 1, 2]
# create object
filtered = filters.filter
# set filter parameter
filtered.ewma_filter_reset(0.2)
# print input and filtered values
for i in range ( len(input_data) ):
  print('input= ' + input_data[i] + ' output= ' + filtered.ewma_filter(input_data[i]) )
```
### other examples
link to more advanced [examples](./examples)


## Average filter

```
average_filter_reset(nums=1)
```
Function resets the filter to initial state with optional parameter **nums** (if omnitet then default set 1 samples average calculation).

```
average_set_samples(nums)
```
The function sets the number of data samples for which the mathematical mean will be calculated. **nums** must be greather or equal 1.

```
average_filter(input)
```
The function returns the calculated value for the given **input** data.

## IIR filter

```
iir_filter_reset(factor=1)
```
Function resets the filter to initial state with optional parameter **factor** (if omnitet then default value of factor is set to 1).

```
iir_set_factor(factor)
```
The function sets the factor parameter. **factor** must be greather or equal 1 and should not exceed the value of 32. The factor must be an integer.

```
iir_filter(input)
```
The function returns the calculated value for the given **input** data.

## EWMA filter

```
ewma_filter_reset(alpha=1)
```
Function resets the filter to initial state with optional parameter **alpha** (if omnitet then default value of alpha is set to 1).

```
ewma_set_alpha(alpha)
```
The function sets the alpha parameter. **alpha** must be in range **(0 < alpha < 1)**.

```
ewma_filter(input)
```
The function returns the calculated value for the given **input** data.


### Graphical representation of Average filter working

How the **nums** of samples parameter affects the output.

X axis - number of data sample

Y axis - data value

![res/average_data.png](res/average_data.png)

![res/average_sinus.png](res/average_sinus.png)

### Graphical representation of EWMA filter working

How the **alpha** parameter affects the output.

X axis - number of data sample

Y axis - data value

![res/ewma_data.png](res/ewma_data.png)

![res/ewma_sinus.png](res/ewma_sinus.png)

### Graphical representation of IIR filter working

How the **factor** parameter affects the output.

X axis - number of data sample

Y axis - data value

![res/iir_data.png](res/iir_data.png)

![res/iir_sinus.png](res/iir_sinus.png)
