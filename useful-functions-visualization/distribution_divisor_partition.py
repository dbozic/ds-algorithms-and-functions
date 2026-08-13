def distribution_divisor_partition(series):
  
  """
  Takes in a pandas series of numerical values and prepares
  the series for histogram plotting by finding the difference 
  between int(max(series)) and int(min(series)), followed by finding the list of positive divisors.
  The goal is to produce a list of ordered positive divisors so that
  the appropriate one can be selected as the number of bins in histogram plotting.
  Assumes pandas and numpy as np have been imported. 
  
  INPUT:
  
  series: a pandas series
  
  OUTPUT:
  
  divisors: a list of divisors
  """
  
  maxval = int(np.max(series)) - int(np.min(series))
  divisors = []
  for i in range(1, maxval + 1): # + 1 added to include maximum value in the iteration as positive divisor
    if maxval % i == 0:
      divisors.append(i)
    else:
      pass
  return(divisors)
