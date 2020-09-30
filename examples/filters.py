class filter:

  # EWMA filter
  ewma_has_initial = False
  ewma_alpha = 1
  ewma_output = 0

  def ewma_filter_reset(alpha=1):
    filter.ewma_alpha = alpha
    filter.ewma_output = 0
    filter.ewma_has_initial = False

  def ewma_set_alpha(alpha):
    filter.ewma_alpha = alpha

  def ewma_filter(input):
    if filter.ewma_has_initial:
      filter.ewma_output = filter.ewma_alpha * (input - filter.ewma_output) + filter.ewma_output
    else:
      filter.ewma_output = input
      filter.ewma_has_initial = True
    return filter.ewma_output

  # IIR filter
  iir_output = 0
  iir_factor = 1
  iir_has_initial = False

  def iir_filter_reset(factor=1):
    filter.iir_output = 0
    filter.iir_factor = factor
    filter.iir_has_initial = False

  def iir_set_factor(factor):
    filter.iir_factor = factor

  def iir_filter(input):
    if filter.iir_has_initial:
      filter.iir_output = ( ( (filter.iir_output*(filter.iir_factor-1)) + input) / (filter.iir_factor) )
      return filter.iir_output
    else:
      filter.iir_output = input
      filter.iir_has_initial = True
      return input

  # Average filter
  average_samples = 1
  average_table = []
  average_has_initial = False

  def average_filter_reset(nums = 1):
    filter.average_samples = nums
    filter.average_table = []
    filter.average_has_initial = False

  def average_set_samples(nums):
    filter.average_samples = nums

  def average_filter(input):
    if filter.average_has_initial:
      sum = 0
      filter.average_table.append(input)
      filter.average_table.pop(0)
      for i in range (len(filter.average_table)):
        sum = sum + filter.average_table[i]
      return float(sum/filter.average_samples)
    else:
      filter.average_table = [input] * filter.average_samples
      filter.average_has_initial = True
      return input


