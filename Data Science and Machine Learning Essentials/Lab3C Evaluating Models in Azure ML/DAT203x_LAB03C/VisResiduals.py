def rmse(Resid):
    import numpy as np
    resid = Resid.as_matrix()
    length = Resid.shape[0]
    return np.sqrt(np.sum(np.square(resid)) / length)
    
    
def azureml_main(frame1): 
    # Set graphics backend
    import matplotlib
    matplotlib.use('agg')  
     
    import pandas as pd
    import pandas.tools.rplot as rplot
    import matplotlib.pyplot as plt
    import statsmodels.api as sm

## Compute the residuals
    frame1['Resids'] = frame1['Heating Load'] - frame1['Scored Labels']      
 
## Create data frames by Overall Height   
    temp1 = frame1.ix[frame1['Overall Height'] == 7]    
    temp2 = frame1.ix[frame1['Overall Height'] == 3.5] 
    
## Create a scatter plot of residuals vs Heating Load.
    fig1 = plt.figure(1, figsize=(9, 9))
    ax = fig1.gca()
    temp1.plot(kind = 'scatter', x = 'Heating Load', \
                y = 'Resids', c = 'DarkBlue', alpha = 0.3, ax = ax)
    temp2.plot(kind = 'scatter', x = 'Heating Load', \
                y = 'Resids', c = 'Red', alpha = 0.3, ax = ax)
    ax.set_title('Heating load vs. model residuals')
    plt.show()
    fig1.savefig('plot1.png')
    
## Scatter plots of the residuals conditioned by 
## several features
    col_list = col_list = ["Relative Compactness",
              "Surface Area",
              "Wall Area",
              "Roof Area",
              "Glazing Area"]              
    
    for col in col_list: 
        ## First plot one value of Overall Height.
        fig = plt.figure(figsize=(10, 4.5))
        fig.clf()
        ax = fig.gca()
        plot = rplot.RPlot(temp1, x = 'Heating Load', y = 'Resids') 
        plot.add(rplot.GeomScatter(alpha = 0.3, colour = 'DarkBlue'))
        plot.add(rplot.TrellisGrid(['.', col]))
        ax.set_title('Residuals by Heating Load and height = 7 conditioned on ' + col + '\n')
        plot.render(plt.gcf())
        fig.savefig('scater_' + col + '7' + '.png')
        
        ## Now plot the other value of Overall Height.
        fig = plt.figure(figsize=(10, 4.5))
        fig.clf()
        ax = fig.gca()
        plot = rplot.RPlot(temp2, x = 'Heating Load', y = 'Resids') 
        plot.add(rplot.GeomScatter(alpha = 0.3, colour = 'Red'))
        plot.add(rplot.TrellisGrid(['.', col]))
        ax.set_title('Residuals by Heating Load and height = 3.5 conditioned on ' + col + '\n')
        plot.render(plt.gcf())
        fig.savefig('scater_' + col + '3.5' + '.png')
    
## QQ Normal plot of residuals    
    fig3 = plt.figure(figsize = (12,6))
    fig3.clf()
    ax1 = fig3.add_subplot(1, 2, 1)
    ax2 = fig3.add_subplot(1, 2, 2) 
    sm.qqplot(temp1['Resids'], ax = ax1)
    ax1.set_title('QQ Normal residual plot \n with Overall Height = 3.5')
    sm.qqplot(temp2['Resids'], ax = ax2)
    ax2.set_title('QQ Normal residual plot \n with Overall Height = 7')
    fig3.savefig('plot3.png')

## Histograms of the residuals
    fig4 = plt.figure(figsize = (12,6))
    fig4.clf()
    ax1 = fig4.add_subplot(1, 2, 1)
    ax2 = fig4.add_subplot(1, 2, 2)   
    ax1.hist(temp1['Resids'].as_matrix(), bins = 40)
    ax1.set_xlabel("Residuals for Overall Height = 3.5")
    ax1.set_ylabel("Density")
    ax1.set_title("Histogram of residuals")
    ax2.hist(temp2['Resids'].as_matrix(), bins = 40)
    ax2.set_xlabel("Residuals of model")
    ax2.set_ylabel("Density")
    ax2.set_title("Residuals for Overall Height = 7")
    fig4.savefig('plot4.png')

    
    out_frame = pd.DataFrame({ \
      'rmse_Overall' : [rmse(frame1['Resids'])], \
      'rmse_35Height' : [rmse(temp1['Resids'])], \
      'rmse_70Height' : [rmse(temp2['Resids'])] }) 
    
    return out_frame
  