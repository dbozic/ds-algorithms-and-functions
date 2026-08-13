def manual_histogram (series, figsize, color, edgecolor, xlabel, ylabel, xfontsize, yfontsize, xweight, yweight, 
range_start, range_end, bincount, stepsize, yticks):  
  
  """
  This function takes in a pandas series and plots a manual histogram. 
  Unlike the automatic_histogram.py function, this one requires that you 
  manually inspect max value of a pandas series and decide how many bins
  you want to see in a histogram and what the step size is. 
    
  INPUT:
    
  series: pandas series to be plotted on histogram
  figsize: tuple that denotes figure size, e.g. (10, 5)
  color: string that denotes the color of the plot, e.g. 'blue' or '#000000'
  edgecolor: string that denotes the color of the edge around the bars, e.g. 'blue' or '#000000'
  xlabel: string that denotes the x-axis label, e.g. 'Value in array'
  ylabel: string that denotes the y-axis label, e.g. '% of values'
  xweight: string denoting the type of font thickness, e.g. 'bold' for x-axis
  yweight: string denoting the type of font thickness, e.g. 'bold' for y-axis
  xfontsize: int that denotes size of font used for the x-axis label, e.g. 12
  yfontsize: int that denotes size of font used for the y-axis label, e.g. 12
  range_start: int that denotes where the histogram starts, e.g. 0
  range_end: int that denotes where the histogram ends, e.g. 100
  bincount: int that denotes how many bin counts you want to have 
  stepsize: number that denotes spacing in the bin, e.g. 0.5
  yticks: list of values to be displayed on y-axis, e.g. [0, 5, 10, 15] -- you can uncomment if you don't want to control
  
  OUTPUT:
    
  a plt plot
  """
  
  fig, ax = plt.subplots(figsize = figsize)
  ax.hist(series, color = color, edgecolor = edgecolor, range = (range_start, range_end), bins = bincount)
  ax.set_ylabel(ylabel, weight = yweight, fontsize = yfontsize)
  ax.set_xlabel(xlabel, weight = xweight, fontsize = xfontsize)
  plt.xticks(np.arange(range_start, (range_end + stepsize), stepsize))
  plt.yticks(yticks)
  plt.show()
