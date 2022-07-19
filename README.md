# predict-wind-turbine-energy-output
In this simple project, I have used two different machine learning algorithms in creating a model which can be used to predict the output energy of a wind turbine based on three independent parameters. 
I have obtained the dataset from Kaggle: https://www.kaggle.com/datasets/berkerisen/wind-turbine-scada-dataset
From my analysis on the dataset, I observed that the active power of the wind turbine which is our primary target is dependent on three major values which are:  
- Wind Speed (m/s)
- Wind Direction (°) and 
- Theoretical_Power_Curve (KWh)

However, the date/time column was provided, as all parameters (dependent and independent) were recorded throughout the year of 2018 at an interval of 10 mins from the first 10mins of Jan 1 2018 to the last 10mins of Dec 31 2018. 
Although, I used Google sheet in formatting and further visualizing the dataset and I figured that there were missing data points from:
** 2018-01-26 06:20:00  -  2018-01-30 14:40:00 **. 
 ** 2018-09-28 21:20:00  -  2018-10-02 16:30:00 **
 ** 2018-11-10 21:10:00  -  2018-11-14 12:00:00 ** 
 
 In this project, I have used only two machine learning algorithms which are the Linear Regressor and Random Forest Regressor. The Linear Regressor yielded predictions at an accuracy of approximately 90.38% while the Random Forest Regressor yielded predictions at an accuracy of approximately 90.92%. 
At this point, it is important to note that this models were not built based on time series analysis. That is, the predictions are not based on times during the year, but primarily the wind speed, wind direction at anytime in the year and theoretical power curve of the proposed wind turbine. Due to my experience from some field work in various climate, I have learnt that weather forecast throughout the year could be influenced by a lot of factors which could change predictions. 
