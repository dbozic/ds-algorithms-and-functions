def identify_bin_count(divisors):
  
  """
  The function is intended to take in a list of ordered positive 
  divisors and find the appopriate number-of-bins value for histogram plotting. 
  The function returns the item from the list that is one position greater than
  the arithmetic middle. The logic, if necessary, can be adjusted in the function 
  by adding or subtracting (n) within the return portions.
  
  INPUT: 
  
  divisors: a list of divisors, presumably produced by the distribution_divisor_partition.
  
  OUTPUT:
  
  bin_count = an integer that will represent spacing of bins.
  """
  
  if int(len(divisors)) % 2 == 0:
    bin_count = divisors[(len(divisors) // 2)]
  else:
    bin_count = divisors[(math.ceil(len(divisors) / 2))]
  return(bin_count)
