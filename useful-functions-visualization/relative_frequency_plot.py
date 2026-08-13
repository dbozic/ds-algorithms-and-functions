def relative_frequency_plot(data, group_class, grouped_variable, figsize, legend, color, title, fontsize, tickfontsize, weight,
    xtitle, xfontsize, xweight, ytitle, yfontsize, yweight, yticks, xrotation, sort, top):
      
    """
    This function takes in a pandas dataframe and plots a relative frequency
    bar plot. The function requires that the dataframe is passed through 
    untransformed, because the function will perform aggregation. You will have the option 
    to specify whether you want the chart to be sorted by Descending values, and if you 
    want to select only top "N" instances, in cases when you have too many categorical variables.
    
    INPUT:
    
    data: pandas dataframe
    grouped_class: variable that will be used as basis for grouping - this will be the x-axis on plot
    grouped_variable: variable that will be used for aggregation, e.g. member_id, account_id
    figsize: tuple that denotes figure size, e.g. (10, 5)
    legend: boolean to denote whether legend needs to be shown
    color: string that denotes the color of the plot, e.g. 'blue' or '#000000'
    title: string that denotes the title of the plot, e.g. 'CDF of values in array'
    fontsize: integer denoting size of font used in text of the plot, e.g. 12
    tickfontsize: integer denoting size of font used in x- and y-ticks, e.g. 12
    weight: string denoting the weight of font in the title, e.g. 'bold'
    xtitle: string that denotes the x-axis label, e.g. 'Value in array'
    xfontsize: see fontsize, applied to x-axis
    xweight: see weight, applied to x-axis
    ytitle: string that denotes the y-axis label, e.g. '% of values'
    yfontsize: see fontsize, applied to y-axis
    yweight: see weight, applied to y-axis
    yticks: manual setting of y-ticks, useful when comparing multiple charts, e.g. [0, 5, 10, 15, 20]
    xrotation: integer denoting the angle of rotation of x-ticks, e.g. 85
    sort: boolean denoting if the variable should be ordered by Descending frequency, e.g. True/False
    top: Use an integer if you want to plot only top X instances, e.g. 20 for top 20 instances. Use False if you want to plot everything.
    
    OUTPUT:
    
    a bar plot

    """
    
    # Number of instances per each group-by class 
    count_per_group_class = data.groupby(group_class)[[grouped_variable]].count()
    
    # Count the total number of instances 
    count_of_instances = count_per_group_class.sum()
    
    # Transform the variable into percentage of instances per group-by-class
    percentage_per_group_class = count_per_group_class.divide(count_of_instances).multiply(100).round(decimals = 1)
    
    # Plot the instance distribution data
    
    # Sort if argument passed
    if sort == True:
      percentage_per_group_class = percentage_per_group_class.sort_values(by = [grouped_variable], ascending = False)
    else:
      pass
    
    # Select only top instances if argument passed
    if top == False:
      pass
    else:
      percentage_per_group_class = percentage_per_group_class.head(top)
      
    # Plot
    ax = percentage_per_group_class.plot.bar(figsize = figsize, legend = legend, color = color, fontsize = tickfontsize, rot = xrotation)
    ax.set_title(title, fontsize = fontsize, weight = weight)
    ax.set_xlabel(xtitle, fontsize = xfontsize, weight = xweight)
    ax.set_ylabel(ytitle, fontsize = yfontsize, weight = yweight)
    ax.set_yticks(yticks)
 
    # Annotate bar plots if necessary; if not, uncomment the following lines
    for p in ax.patches:
      ax.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
