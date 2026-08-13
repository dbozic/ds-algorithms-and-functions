def greatest_divisor_of_middle(ordered_numbers):
  
  """
  The function is intended to take in a list of non-zero ordered numbers, find
  the middle value, and then find the greatest divisor of that number in the list. 
  The function was originally designed to partition histogram bins and find appropriate spacing,
  but can be extracted for general purpose and other potential plotting purposes. 
  
  INPUT: 
  
  ordered_numbers: a list of ordered non-zero numbers. 
  
  OUTPUT:
  
  bins: a list where [0] = middle value and [1] = greatest divisor of that value within the list.
  """
  
  # if the length of the list is even 
  
  if int(len(ordered_numbers)) % 2 == 0:
    # pick the greatest number in the list that's lesser than arithmetic middle
    middle = ordered_numbers[(len(ordered_numbers) // 2) - 1] # subtract 1 due to pythonic indexic
    divisors = []
    # identify all divisors of the middle number within the list
    for i in ordered_numbers:
      if int(middle % i) == 0:
        if i < middle:
          divisors.append(i)
        else:
          pass
      else:
        pass
      
  # if the length of the list is odd
  
  else:
    # pick the midde number
    middle = ordered_numbers[(math.ceil(len(ordered_numbers) / 2)) - 1] # subtract 1 due to pythonic indexing
    divisors = []
    # identify all divisors of the middle number within the list
    for i in ordered_numbers:
      if int(middle) % i == 0:
        if i < middle:
          divisors.append(i)
        else:
          pass
      else:
        pass
  # choose the maximum as the greatest divisor of the middle number
  bins = [middle, max(divisors)]
  return(bins)
