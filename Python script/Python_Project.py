# Using the below data and writing Python code produce the following results
    # 1. Resultant file with name and total scores for each student.
    # 2. Another file with top scorer’s name, subject and score in each subject.

# Student_name,subj1,score1,subj2,score2
# abc,math,89,science,91
# xyz,math,90,science,95
# cde,math,86,science,78

# Importing necessary packages into Python.

import pandas as pd #Loading Panda build data and to peform any data analysis opertations

# Create the list
data = {'Student_name': ['abc', 'xyz', 'cde'], 'subj1': ['math', 'math', 'math'], 'score1': [89, 90,86], 'subj2': ['science', 'science', 'science'],'score2': [91, 95,78]}

# Converting list into a data frame
df = pd.DataFrame(data)  

# Converting the dataframe from a wide format to a long format for easy analysis of data.
# Creating two datasets by pulling Sub1 and Sub2 separately
df1 = df[['Student_name','subj1','score1']]
df2 = df[['Student_name','subj2','score2']]

# Renaming the columns to standard names
df1.columns =['Student_name', 'Subject_Name', 'Score']
df2.columns =['Student_name', 'Subject_Name', 'Score']

# Appending the two datasets into one dataset
Final_df = df1.append(df2, sort=False)

# Indexing the column names
#Final_df = Final_df.reindex(columns=['Student_name', 'Subject_Name', 'Score'])

# Calculating the total scores for each student and adding the result back to the data frame
First_result = Final_df.groupby(['Student_name']).agg({'Score': "sum"})

# Exporting the First results to a csv file
First_result.to_csv('first_result.csv', sep=',')

# Rank ordering the scores by subject and by student to get students with highest score in each subject
Final_df['Rank'] = Final_df.groupby(['Subject_Name'])['Score'].rank(method='max', ascending = False)

# Filtering on students that scored highest in both Maths and Science
Second_result = Final_df.loc[Final_df.Rank == 1, ["Student_name", "Subject_Name", "Score"]]

# Exporting the First results to a csv file
Second_result.to_csv('second_result.csv', sep=',',index=False)
