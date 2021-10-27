
import pandas as pd
#To read csv file I used pandas library.
#To parse the data in csv file (pd.read_csv) is used. 
 
df = pd.read_csv("StudentsPerformance.csv")
#Data in csv file are fetched to dataframe(df).
 
df = df.head()
#head() returns gest of dataframe(df).

df.to_json("StudentsPerformance_summary")
#dataframe(df) is converted into json.
