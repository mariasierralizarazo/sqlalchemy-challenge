# SQLAlchemy-challenge
The main goal of this challenge is to use SQLAlchemy module in Python to query, analyze, and get information related to the wheater in Hawaii on specific dates. <br/> 
Dependencies used: <br/>
- SQLalchemy <br/>
- Pandas <br/>
- Matplotlib <br/>
- Datetime <br/>

SQLAlchemy is a module that will create a "virtual object database" from the original database (Resources\hawaii.sqlite). 
This enables reading and querying the information in the database using python language. <br/>
##### Note: SQLAlchemy is flexible in the way that querying can be done. It could be using more SQL or more Pyhton syntaxis. For this project, more Python syntaxis was used. <br/>
The first step was to create a session to the database and identify the classes (tables) inside. Once that was done, it was possible to recognize with the inspector tool the columns name and the data types in those columns. The following results were obtained: <br/>
<p align="center">
  <img width="560" height="250" src="https://github.com/mariasierralizarazo/sqlalchemy-challenge/blob/master/figures/tables.png">
</p>
Having the database's description with each table and their columns, the next step was to show the performance of the precipitation levels in Hawaii in the last year register in the data.   So, it was necessary to recognize the last date registered in the data and make the analysis starting 365 days before it. As a result, it was possible to see in a graph the precipitation levels in inches per day where some spikes are distinguished around September, February, and between May and June. After that, some summary statistics were calculate using DataFrames structures.<br/>
<br/>
<p align="center">
  <img width="660" height="450" src="https://github.com/mariasierralizarazo/sqlalchemy-challenge/blob/master/figures/precipitation_figure.png">
</p>
<br/>
After the precipitation analysis in the last year of data, a temperature analysis was done in the same period; however, for this new examination of the data, stations were taken into account. In that way, it was necessary to recognize the stations that had information related to the last year and the number of datapoints the database had for each station. Next, in the most active station (the one with a higher number of data points) the minimum, the maximum, and the average temperature values were calculated.
Finally, for the most active station, a histogram with 12 bins was plotted, having a larger concentration in temperatures between 77°F and 80°F.<br/>
<br/>
<p align="center">
  <img width="660" height="450" src="https://github.com/mariasierralizarazo/sqlalchemy-challenge/blob/master/figures/histogram_temp.png">
</p>
<br/>
Continuing with the data exploration, two specific dates were selected - the idea was to select a random period of time for having a vacation in Hawaii for at least 15 days-, and in those days the general average temperature was calculated and plotted in the following graph.<br/>
<br/>
<p align="center">
  <img width="660" height="450" src="https://github.com/mariasierralizarazo/sqlalchemy-challenge/blob/master/figures/AverageTemperature.png">
</p>
<br/>
The dates selected were March 15 and April 06, 2017, where the average temperature was 73.64 °F, the minimum was  65°F, and the maximum was  80 °F. The y error bar in black represents the difference between the maximum and the minimum temperature. 
<br/><br/>
For the end of this analysis, daily normals were calculated and plotted too. These calculations give as a result the minimum and maximum measured temperature per day having the information in all the stations, and the average temperature calculated with the register data in all the stations too. This allows seeing the difference between these three values in a no stacked area plot where it is possible to see the fluctuation in the temperature the days of the trip.  
<br/><br/>
<p align="center">
  <img width="660" height="450" src="https://github.com/mariasierralizarazo/sqlalchemy-challenge/blob/master/figures/normals_values.png">
</p>
<br/>
[Go to the Jupyter Notebook with the code](https://github.com/mariasierralizarazo/sqlalchemy-challenge/blob/master/climate.ipynb)
<br/>
Another useful application in this project was created using Flask a micro web framework that allowed the generation of an API of the database given. [Click here to see the code] (https://github.com/mariasierralizarazo/sqlalchemy-challenge/blob/master/app.py)
<br/>
