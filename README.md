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
  <img width="660" height="250" src="https://github.com/mariasierralizarazo/sqlalchemy-challenge/blob/master/figures/tables.png">
</p>
