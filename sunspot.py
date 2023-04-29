import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

indata=pd.read_csv("sunspots.csv")
print("indata",indata.head())
print("Sunspots dataset notes",sm.datasets.sunspots.NOTE) 
print(dir(sm.datasets.longley)) #gives the details of the longley dataset
print(dir(sm.datasets.sunspots))#gives the details of the sunspots dataset
print(dir(sm.datasets)) #gives the details of all the available datasets inside the
                        # statsmodels readymade datasets.
print("indata",indata) #we can see that the data is captured for each year from 1700
                        #to 2008 which is shown by Year column 
#Now we need to prepare the data in required date format for performing time series 
#Now let us generate the date in YYYYMMDDHHMM for starting from 1700 to 2008 year
#And set this generated date as index and remove the Year colum 
print("sm.tsa.datetools.dates_from_range('1700', '2008')", 
      sm.tsa.datetools.dates_from_range('1700', '2008'))   
    #This will generate the dates as datetime.datetime(1700, 12, 31, 0, 0), 
    # datetime.datetime(1701, 12, 31, 0, 0),
    # datetime.datetime(1702, 12, 31, 0, 0)...etc till 2008,12,31,0,0) i.e. yearly date
    # for each year  
indata.index=pd.Index(sm.tsa.datetools.dates_from_range("1700", '2008'))
print(indata.head())
del indata['YEAR']
print(indata.head())

#Now plot and see the data for any repetative patterns
#we need to examine the data to see if it is fit for time series or not
#for that we need to plot the graph
indata.plot(figsize=(12,10))    
plt.show()                                    


#Perform Durbin Watson test to check serial correlation present or not
#For the time series to be performed there should not be serial correlation present

print(sm.stats.durbin_watson(indata))
#Here we got the durbin watson statistics value as 0.13952893
# This indicates there is a autocorrelation present. (value close to 2 is considered as
# no correlation). value less than 2 means possitive correlation, greater than 2 
#means negative correlation.

#Let us plot the ACF and PACF plots for the observation
# show plots in the notebook

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(indata.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(indata, lags=40, ax=ax2)
plt.show()