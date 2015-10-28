def azureml_main(frame1):
## import libraries
    import matplotlib
    matplotlib.use('agg')  # Set backend
    
    from pandas.tools.plotting import scatter_matrix
    import pandas.tools.rplot as rplot
    import matplotlib.pyplot as plt
    import numpy as np
 
## Create a pair-wise scatter plot    
    fig1 = plt.figure(1, figsize=(10, 10))
    ax = fig1.gca()
    scatter_matrix(frame1, alpha=0.3, 
                   diagonal='kde', ax = ax)
    plt.show()
    fig1.savefig('scatter1.png')

## Create conditioned scatter plots.    
    col_list = ["Relative Compactness",
               "Surface Area",
               "Wall Area",
               "Relative Compactness Sqred",
               "Surface Area Sqred",
               "Wall Area Sqred",
               "Relative Compactness 3",
               "Surface Area 3",
               "Wall Area 3",
               "Roof Area",
               'Glazing Area',
               "Glazing Area Distribution"]

    indx = 0
    for col in col_list:
        if(frame1[col].dtype in [np.int64, np.int32, np.float64]):
            indx += 1
            
            fig = plt.figure(figsize = (12,6))
            fig.clf()
            ax = fig.gca()
            plot = rplot.RPlot(frame1, x = col, y = 'Heating Load')
            plot.add(rplot.TrellisGrid(['Overall Height','Orientation']))
            plot.add(rplot.GeomScatter())
            plot.add(rplot.GeomPolyFit(degree=2))
            ax.set_xlabel(col)
            ax.set_ylabel('Heating Load')
            plot.render(plt.gcf())
            
            fig.savefig('scatter' + col + '.png')
 
## Histograms of Heating Load by Overall Height
    col_list = ["Relative Compactness",
               "Surface Area",
               "Wall Area",
               "Relative Compactness Sqred",
               "Surface Area Sqred",
               "Wall Area Sqred",
               "Relative Compactness 3",
               "Surface Area 3",
               "Wall Area 3",
               "Roof Area",
               'Glazing Area',
               "Glazing Area Distribution",
               "Heating Load"]
    for col in col_list:
        temp7 = frame1.ix[frame1['Overall Height'] == 7, col].as_matrix()
        temp35 = frame1.ix[frame1['Overall Height'] == 3.5, col].as_matrix()  
        fig = plt.figure(figsize = (12,6))
        fig.clf()
        ax7 = fig.add_subplot(1, 2, 1)
        ax35 = fig.add_subplot(1, 2, 2) 
        ax7.hist(temp7, bins = 20)
        ax7.set_title('Histogram of ' +col + '\n for for Overall Height of 7')
        ax35.hist(temp35, bins = 20)
        ax35.set_title('Histogram of ' +col + '\n for for Overall Height of 3.5')
        fig.savefig('hists_' + col + '.png')
   

## Creat boxplots.    
    for col in col_list:
        if(frame1[col].dtype in [np.int64, np.int32, np.float64]):                  
            fig = plt.figure(figsize = (6,6))
            fig.clf()
            ax = fig.gca() 
            frame1[[col, 'Overall Height']].boxplot(column = [col], ax = ax, by = ['Overall Height'])
            ax.set_xlabel('')
            fig.savefig('box_' + col + '.png')

## Return the data frame
    return frame1

