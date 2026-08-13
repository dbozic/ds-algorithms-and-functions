def plot_multiple_relative_frequency_plots(data, variables, grouped_variable, figsize, legend, color, title, fontsize, tickfontsize, weight,
    xfontsize, xweight, ytitle, yfontsize, yweight, yticks, xrotation, sort, top):
  
 """
 This function uses the relative_frequency_plot and automates plotting of multiple charts
 when you need to visualize relative frequency plots for a bunch of variables. You will 
 use the same arguments as relative_frequency_plot, and there will be new ones this time:
 
 INPUTS: 
 
 variables: a list of strings, where each string denotes the name of the column/variable
  in the pandas dataframe you want to visualize

 OUTPUT: 
 
 multiple relative frequency plots
 
 """
 for variable in variables:
   
  relative_frequency_plot(
    data = data, 
    group_class = variable,
    grouped_variable = grouped_variable,
    figsize = figsize,
    legend = legend, 
    color = color, 
    title = title, 
    fontsize = fontsize, 
    tickfontsize = tickfontsize, 
    weight = weight,
    xtitle = variable, 
    xfontsize = xfontsize, 
    xweight = xweight, 
    ytitle = ytitle, 
    yfontsize = yfontsize, 
    yweight = yweight, 
    xrotation = xrotation, 
    sort = sort, 
    top = top,
    yticks = yticks
    
  )
