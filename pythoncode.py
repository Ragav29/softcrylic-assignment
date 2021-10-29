import pandas as pd
import json

#reding the csv file
df = pd.read_csv("StudentsPerformance.csv")
#calculation of averages
average_math = (df[['math score']].mean()).to_string(index=False)
average_read = (df[['reading score']].mean()).to_string(index=False)
average_write = (df[['writing score']].mean()).to_string(index=False)
#education value list
unique_value = list(df['parental level of education'].unique())

ragav ={
    "education_level":unique_value,
    "scores" : {
        "average":{
            "math_score":average_math,
            "reading_score":average_read,
            "writing_score":average_write
        }
    }
}

with open("students_performance_summary.json","w") as json_file:
    json.dump(ragav,json_file)


