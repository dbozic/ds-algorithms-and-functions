def relative_frequency_comparative_plot(dataframe, figsize, colors, xvariable, yvariable, xtitle, ytitle, xlabelfontsize, ylabelfontsize, xtickfontsize, ytickfontsize, legendsize):
  
  """
  This function takes in a pandas dataframe and plots a comparative frequency plot of 
  a single indepdent variable against a dependent variable. 
    
  INPUT:
  
  dataframe: name of the dataframe you will be analyzing, e.g. customers
  colors: dictionary that assigns colors to each value of a dependent variable, e.g. {'Current': "blue", 'Lost': "#4E79A7"} - means you have to specify outputs of dv 
  xvariable: name of the independent variable you want to see on the x-axis, needs to be surrounded with "", e.g. "COMPANY_STATE"
  yvariable: name of the dependent variable you want to see independent variable distinguished by, needs to be surrounded with "", e.g. "CUSTOMER_TYPE"
  xtitle: string that denotes the x-axis label, e.g. 'Value in array'
  ytitle: string that denotes the y-axis label, e.g. '% of values'
  xlabelfontsize: int that denotes size of font used for the x-axis, e.g. 12
  ylabelfontsize: int that denotes size of font used for the y-axis, e.g. 12
  xtickfontsize: int that denotes size of font used for x-ticks, e.g. 12
  ytickfontsize: int that denotes size of font used for y-ticks, e.g. 12
  legendsize: int that denotes size of plot label, e.g. 20

  OUTPUT:
    
  a plt plot

  """
  df = dataframe
  colors = colors
  
  fig, ax = plt.subplots(figsize = figsize)
  (
    df[xvariable]
    .groupby(df[yvariable])
    .value_counts(normalize=True).multiply(100)
    .rename(ytitle)
    .reset_index()
    .pipe((sns.barplot, "data"), x=xvariable, y = ytitle, hue=yvariable, palette = colors)
  )
  ax.set_xlabel(xtitle, fontsize = xlabelfontsize)
  ax.set_ylabel(ytitle, fontsize = ylabelfontsize)
  plt.xticks(fontsize = xtickfontsize)
  plt.yticks(fontsize = ytickfontsize)
  ax.legend(prop={'size': legendsize})
