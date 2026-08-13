def bar_vs_line_plot (figsize, bar_variable, line_plot_variable_1, line_plot_variable_2, bar_variable_color, 
line_plot_variable_1_markersize, line_plot_variable_1_color, line_plot_variable_1_label,
line_plot_variable_2_markersize, line_plot_variable_2_color, line_plot_variable_2_label,
plot_title, titlefontsize,
bar_variable_yticklabels, bar_variable_ytick_fontsize,
bar_variable_ylabel, bar_variable_yaxis_fontsize,
xvariable, xtickfontsize, xtickrotation,
line_variable_ylabel, line_variable_yaxis_fontsize,
line_variable_yticklabels, line_variable_ytick_fontsize,
legendsize):
  
  """
  
  A useful function for plotting bar-chart and line plots together when a relationship wants to be shown.
  This function takes in one bar-chart variable and two line-plot variables but can be adjusted if more lines
  need to be shown. It assumes that the two line-chart variable will have the same scale as they will be shown on the 
  right-hand side y-axis.
  
  INPUT: 
  
  figsize: Size of the figure, e.g. (15, 10),
  bar_variable: name of the pandas column that will be plotted as the bar variable,
  line_plot_variable_1: name of the pandas column that will be plotted as the first line variable,
  line_plot_variable_2: name of the pandas column that will be plotted as the second line variable,
  bar_variable_color: color of the bar variable, e.g. '#209cfa',
  line_plot_variable_1_markersize: size of the marker used for first line variable, e.g. 12,
  line_plot_variable_1_color: color of the first line variable, e.g. '#ff604a',
  line_plot_variable_1_label: label that will be shown in the legend for first line variable, e.g. 'Cancelation %',
  line_plot_variable_2_markersize: size of the marker used for first line variable, e.g. 12,
  line_plot_variable_2_color: color of the second line variable, e.g. '#ff604a',
  line_plot_variable_2_label: label that will be shown in the legend for second line variable, e.g. 'Completion %',,  
  plot_title: label of the plot, 'Test',
  titlefontsize: font size used on the plot label, e.g. 14,
  bar_variable_yticklabels: specified y-labels for the bar-variable, e.g. [0, 1000, 2000, 3000, 4000, 5000],
  bar_variable_ytick_fontsize: font size used on yticks for the bar variable, e.g. 14, 
  bar_variable_ylabel: label for the y-axis of the bar variable,
  bar_variable_yaxis_fontsize: font size of the y-axis label of the bar variable, e.g. 16, 
  xvariable: name of the pandas variable that will be used for plotting, which gets converted to a list by the function first
  xtickfontsize: size of the xticks, e.g. 12, 
  xtickrotation: rotation angle for the x-ticks, e.g. -30, 
  line_variable_ylabel: ylabel of the line variables, 
  line_variable_yaxis_fontsize: font size used for the y-axis label of the line variables, e.g. 12, 
  line_variable_yticklabels: specified y-tick labels for the line variable, e.g. percentages like [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
  line_variable_ytick_fontsize: font size used for the yticks of the line variables, e.g. 10, 
  legendsize: size of the plot legend, e.g. 14
  
  OUTPUT:
  
  a plt plot
  """
  
  # Convert x-variable to list for easy plotting
  xticklabels = xvariable.to_list()
  
  # Figure size
  fig, ax1 = plt.subplots(figsize = figsize)
  
  # plot the bar variable against the line variables 
  bar_variable.plot(kind = 'bar', color = bar_variable_color)
  line_plot_variable_1.plot(secondary_y=True, linestyle = '--', marker = 'o', markersize = line_plot_variable_1_markersize, color = line_plot_variable_1_color, label = line_plot_variable_1_label)
  line_plot_variable_2.plot(secondary_y=True, linestyle = '--', marker = 'o', markersize = line_plot_variable_2_markersize, color = line_plot_variable_2_color, label = line_plot_variable_2_label)
  
  # plot title
  plt.title(plot_title, weight = 'bold', fontsize = titlefontsize)
  
  # bar y-axis
  ax1.set_yticklabels(bar_variable_yticklabels, fontsize = bar_variable_ytick_fontsize)
  ax1.set_ylabel(bar_variable_ylabel, weight = 'bold', fontsize = bar_variable_yaxis_fontsize)
  
  # x-axis
  ax1.set_xticklabels(xticklabels, weight = 'bold', fontsize = xtickfontsize, rotation = xtickrotation)
  
  # line y-axis
  plt.ylabel(line_variable_ylabel, weight = 'bold', fontsize = line_variable_yaxis_fontsize)
  plt.yticks(line_variable_yticklabels, fontsize = line_variable_ytick_fontsize)
  
  # chart finesse
  plt.xlim(-1, 10)
  plt.legend(loc = 'lower right', prop = {'size': legendsize})
  plt.show()
