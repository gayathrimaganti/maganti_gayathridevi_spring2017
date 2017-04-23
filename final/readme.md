Data Analysis using Python: Final Project Spring 2017

Selected Pattern: 

Pattern 1(100 Points)

Using a readily downloadable dataset, perform 5 analysis on the dataset and create a Readme.md file explaining your analysis. 

Project Topic: 911 Emergency calls

Dataset: 911 Emergency calls of Montgomery County, Pennsylvania, USA beginning from December 2015 to present.

Link from which Dataset has been downloaded: http://montcoalert.org/gettingdata/ (Data is updated daily at this URL)

Dataset path in folder(GitHub): final/data/911.csv


Analysis 1: 
1.	Read the data from .csv file into a dataframe using pandas.
2.	Displaying the information about the dataframe to find the datatypes and various columns available.

3.	Finding the top 5 most occurring townships in the 911 emergency calls list.
4.	Finding the counts for the top 5 most occurring Zip Codes.
5.	Finding the number of unique titles, i.e. various types of emergency reasons
6.	Counting the number of emergencies for each ‘type’ of emergency from December 2015 to present.
7.	Analyzing the number of townships that got emergency calls for each day.
8.	Finding the number of townships that received emergency calls each day by date only for 'Medical Emergency'.
9.	Finding the number of townships that received emergency calls each day by date only for 'Fire’.
10.	Finding the number of townships that received emergency calls each day by date only for 'Traffic’.
11.	Finally, from the analysis, the graphs show that the ‘Traffic’ type of emergency was the reason for calls to maximum townships in Montgomery County. Its value shows above 500 around the month of February 2016.


Analysis 2:
1.	Analyzing the township which has the highest number of emergency calls.
2.	Finding the various categories of emergency and analyzing the counts of emergencies during an hour, day of the week and month of the year for the year 2016.
3.	Creating another data frame to store the records only with the year 2016 and displaying them.
4.	Creating new columns for the new data frame with hour, day of the week and month of the year using lambda function.
5.	Finding the counts for emergencies for each ‘type’ of emergency in the year 2016.
6.	The results show that Medical Emergencies(EMS) has the highest number of calls followed by Traffic and Fire.
7.	Plotting the graphs for counts of emergency calls for EMS, Traffic and Fire for each Hour, day of the week and month of the year.
8.	Analyzing the number of emergency calls by township in the year 2016 and sorting them by mean value ’e’.
9.	The counts are then grouped by township that is, a bar graph for the mean value and townships has been plotted which shows that ‘Lower Merion’ has the highest mean of emergency calls and township ‘Horsham’ has the least.
10.	This shows that township ‘Lower Merion’ had the highest mean value of number of calls during the year 2016.

Analysis 3: 
1.	Reading the csv using read_csv function in pandas.
2.	Finding the top 20 Zip codes that received most number of emergency 911 calls by using the groupby function on ‘zip’ column and finding the count of calls using the size function and then sorting the values of count which is made the index. Storing these values in a variable top_20 in order to plot a bar graph.
3.	The graph shows that Zip code 19041 had the most number of calls.
4.	Finding the percentage values of calls in each category or for the type of emergency and displaying it in a pie-chart. Medical Emergency has the most. This is found by creating another column called category that stores the ‘type’ split by a colon.
5.	The autopct variable displays the percentages of calls in each category while the pie function takes in sizes as parameters and calculates the percentages.
6.	Finding the call frequency in a day using lambda function to divide time into the 24 hours of the day.
7.	Using np.arange() is used to find the frequency of calls.
8.	Finding the call count for all the categories in the last three months, i.e., Jan, Feb, March 2017 where the counts are stored in 3 variables and grouped by category and storing the count values.
9.	A bar plot is plotted to showed the frequency of call for the categories.
10.	Analysis shows that the three months of 2017 had the maximum number of medical emergencies followed by Traffic and Fire.

Analysis 4 & 5:
1.	Finding the Top 5 emergencies in the dataset with their counts.
2.	Creating categories and sub-categories for the types of emergencies.
3.	Finding the top 5 sub-categories under the category EMS.
4.	Finding the top 5 sub-categories under the category Fire.
5.	Finding the top 5 sub-categories under the category Traffic.
6.	Finding the emergency calls and the time of the day by categorizing as morning, noon, afternoon, evening and Night and finding their counts.
7.	It has been found that maximum emergencies lined up during the morning.
8.	Finding the counts of calls for each day of the week. Sunday has the lowest frequency of calls.
9.	Finding the top 5 places from where 911 calls originated and their frequencies.
10.	Lower Merion seemed to be with most emergencies.
11.	Lower Merion seemed to be most affected by Traffic emergencies.
12.	Finding the Time zone of vehicle accidents at Lower Merion.
13.	The plot shows that vehicle accidents have occurred most during the morning and least in the night.
14.	Now, considering the 5 townships that made lowest number of 911 calls, Lehigh County was found to be the least.
15.	Lehigh County has most emergencies as EMS. Now, finding the number of emergencies under each sub-category.
16.	Plotting the top 10 places for EMS Category.
17.	Plotting the top 10 places for Fire Category.
18.	Plotting the top 10 places for Traffic Category.
19.	From this analysis, it has been found that Township Norristown has higher number of EMS, while low number of Fire and Traffic. Lower Merion has almost similar count for all categories.



  
