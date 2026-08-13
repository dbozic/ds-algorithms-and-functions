def automatic_histogram(series, figsize, color, edgecolor, title, xlabel, ylabel, fontsize, xsize, ysize):
  
  """
  This function takes in a pandas series and plots an automatic histogram. The 
  key component of this functions is that it utilizes two functions to detect the
  appropriate number of bins and correct xticks spacing, which is often problematic
  in matplotlib. Assumes that identify_bin_count and 
  distribution_divisor_partition custom-made functions have been defined. 
    
  INPUT:
    
  series: pandas series to be plotted on histogram
  figsize: tuple that denotes figure size, e.g. (10, 5)
  color: string that denotes the color of the plot, e.g. 'blue' or '#000000'
  edgecolor: string that denotes the color of the edge around the bars, e.g. 'blue' or '#000000'
  title: string that denotes the title of the plot, e.g. 'CDF of values in array'
  xlabel: string that denotes the x-axis label, e.g. 'Value in array'
  ylabel: string that denotes the y-axis label, e.g. '% of values'
  fontsize: int that denotes size of font used for the axes and plot title, e.g. 12
  xsize: int that denotes size of font used on x-axis, e.g. 12
  ysize: int that denotes size of font used on y-axis, e.g. 12
  OUTPUT:
    
  a plt plot
  """
  
  fig, ax = plt.subplots(figsize = figsize)
  ax.hist(series, 
          color = color, 
          edgecolor = edgecolor, 
          range = ( int(np.min(series)), int(np.max(series)) ), 
          bins = identify_bin_count(distribution_divisor_partition(series)))
  ax.set_title(title, weight = 'bold', fontsize = fontsize)
  ax.set_xlabel(xlabel, weight = 'bold', fontsize = fontsize)
  ax.set_ylabel(ylabel, weight = 'bold', fontsize = fontsize)
  plt.xticks(range(
    int(np.min(series)), 
    int(np.max(series)) + (int(np.max(series)) - int(np.min(series))) // identify_bin_count(distribution_divisor_partition(series)),
    (int(np.max(series)) - int(np.min(series))) // identify_bin_count(distribution_divisor_partition(series))), 
    fontsize = xsize)
  plt.yticks(fontsize = ysize)
  plt.show()
