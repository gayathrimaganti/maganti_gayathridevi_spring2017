# Data Analysis using Python: Final Project Spring 2017

## Selected Pattern:
 
## Pattern 1(100 Points):

##  Using a readily downloadable dataset, perform 5 analysis on the dataset and create a Readme.md file explaining your analysis. 

## Project Topic: 911 Emergency calls

# Dataset: 911 Emergency calls of Montgomery County, Pennsylvania, USA beginning from December 2015 to present.

### Link from which Dataset has been downloaded: http://montcoalert.org/gettingdata/ (Data is updated daily at this URL)

### Dataset path in folder(GitHub): final/data/911.csv

# Analysis 1: 
1.	Read the data from .csv file into a dataframe using pandas.
2.	Displaying the information about the dataframe to find the datatypes and various columns available.
![1](https://cloud.githubusercontent.com/assets/25045093/25310649/6d2519d2-27b7-11e7-9a04-e03fe85a0c1e.JPG)
3.	Finding the top 5 most occurring townships in the 911 emergency calls list.

![2](https://cloud.githubusercontent.com/assets/25045093/25310650/7577164e-27b7-11e7-9efc-fda3ecb86b8a.JPG)

4.	Finding the counts for the top 5 most occurring Zip Codes.

![top 5 zips](https://cloud.githubusercontent.com/assets/25045093/25310652/8105610a-27b7-11e7-90f3-6fd0b66cf6c7.JPG)

5.	Finding the number of unique titles, i.e. various types of emergency reasons
6.	Counting the number of emergencies for each ‘type’ of emergency from December 2015 to present.

![type of emergency](https://cloud.githubusercontent.com/assets/25045093/25310654/887aa4b8-27b7-11e7-9e33-92af777627e5.JPG)

7.	Analyzing the number of townships that got emergency calls for each day.
![number of townships per date](https://cloud.githubusercontent.com/assets/25045093/25310655/9b11aa4a-27b7-11e7-9b8c-597325f5e1b7.JPG)

8.	Finding the number of townships that received emergency calls each day by date only for 'Medical Emergency'.
![ems-date](https://cloud.githubusercontent.com/assets/25045093/25310656/a0b2b0f2-27b7-11e7-818f-d6f56dee7d1c.JPG)

9.	Finding the number of townships that received emergency calls each day by date only for 'Fire’.
![fire-date](https://cloud.githubusercontent.com/assets/25045093/25310658/a7076ea2-27b7-11e7-999e-5887418a3183.JPG)

10.	Finding the number of townships that received emergency calls each day by date only for 'Traffic’.
![traffic-date](https://cloud.githubusercontent.com/assets/25045093/25310659/aab6d326-27b7-11e7-87f9-acfef1f5065b.JPG)

11.	Finally, from the analysis, the graphs show that the ‘Traffic’ type of emergency was the reason for calls to maximum townships in Montgomery County. Its value shows above 500 around the month of February 2016.



# Analysis 2:
1.	Analyzing the township which has the highest number of emergency calls.
2.	Finding the various categories of emergency and analyzing the counts of emergencies during an hour, day of the week and month of the year for the year 2016.
3.	Creating another data frame to store the records only with the year 2016 and displaying them.
4.	Creating new columns for the new data frame with hour, day of the week and month of the year using lambda function.
![year hour date](https://cloud.githubusercontent.com/assets/25045093/25310667/caa56828-27b7-11e7-8fce-8899e2fc31e2.JPG)

5.	Finding the counts for emergencies for each ‘type’ of emergency in the year 2016.
![ems-fire-traffic-2016](https://cloud.githubusercontent.com/assets/25045093/25310669/cfb1f282-27b7-11e7-9b5f-4dcf394f0a37.JPG)

6.	The results show that Medical Emergencies(EMS) has the highest number of calls followed by Traffic and Fire.
7.	Plotting the graphs for counts of emergency calls for EMS, Traffic and Fire for each Hour, day of the week and month of the year.

![hour-count](https://cloud.githubusercontent.com/assets/25045093/25310695/17c0ae28-27b9-11e7-95b1-6e11429ceb76.JPG)

![dayweek-count](https://cloud.githubusercontent.com/assets/25045093/25310696/1f14fe36-27b9-11e7-87a9-f5bdd6db6fd0.JPG)

![month-count](https://cloud.githubusercontent.com/assets/25045093/25310697/22bfdd6c-27b9-11e7-9b49-ee07f83d9f7a.JPG)

8.	Analyzing the number of emergency calls by township in the year 2016 and sorting them by mean value ’e’.
![township cumulative e mean](https://cloud.githubusercontent.com/assets/25045093/25310699/33fda6a4-27b9-11e7-9619-3389f2a0509a.JPG)


9.	The counts are then grouped by township that is, a bar graph for the mean value and townships has been plotted which shows that ‘Lower Merion’ has the highest mean of emergency calls and township ‘Horsham’ has the least.
![township-mean graph](https://cloud.githubusercontent.com/assets/25045093/25310702/4211c9e6-27b9-11e7-91fd-1955e312c8b2.JPG)


10.	This shows that township ‘Lower Merion’ had the highest mean value of number of calls during the year 2016.



# Analysis 3: 
1.	Reading the csv using read_csv function in pandas.
2.	Finding the top 20 Zip codes that received most number of emergency 911 calls by using the groupby function on ‘zip’ column and finding the count of calls using the size function and then sorting the values of count which is made the index. Storing these values in a variable top_20 in order to plot a bar graph.

![zip 20](https://cloud.githubusercontent.com/assets/25045093/25310715/d174ac2a-27b9-11e7-95d0-e2e184ba76c0.JPG)

3.	The graph shows that Zip code 19041 had the most number of calls.
4.	Finding the percentage values of calls in each category or for the type of emergency and displaying it in a pie-chart. Medical Emergency has the most. This is found by creating another column called category that stores the ‘type’ split by a colon.

![pie](https://cloud.githubusercontent.com/assets/25045093/25310716/d9060df8-27b9-11e7-8e74-2d39b1e48203.JPG)

5.	The autopct variable displays the percentages of calls in each category while the pie function takes in sizes as parameters and calculates the percentages.
6.	Finding the call frequency in a day using lambda function to divide time into the 24 hours of the day.
7.	Using np.arange() is used to find the frequency of calls.

![call freq in a day](https://cloud.githubusercontent.com/assets/25045093/25310717/e1554dd4-27b9-11e7-865b-aab672b3f723.JPG)

8.	Finding the call count for all the categories in the last three months, i.e., Jan, Feb, March 2017 where the counts are stored in 3 variables and grouped by category and storing the count values.
9.	A bar plot is plotted to showed the frequency of call for the categories.

![calls in last three months](https://cloud.githubusercontent.com/assets/25045093/25310719/e97c5ab6-27b9-11e7-9ec7-3a5bc225e413.JPG)


10.	Analysis shows that the three months of 2017 had the maximum number of medical emergencies followed by Traffic and Fire.

Analysis 4 & 5:
1.	Finding the Top 5 emergencies in the dataset with their counts.
![top 5 emegr](https://cloud.githubusercontent.com/assets/25045093/25310729/1c372a62-27ba-11e7-89e5-124f88b812e4.JPG)

2.	Creating categories and sub-categories for the types of emergencies.
3.	Finding the top 5 sub-categories under the category EMS.

![top 5 ems](https://cloud.githubusercontent.com/assets/25045093/25310730/2ec643e8-27ba-11e7-9442-26adff866c49.JPG)

4.	Finding the top 5 sub-categories under the category Fire.

![top5fire](https://cloud.githubusercontent.com/assets/25045093/25310744/dee3009a-27ba-11e7-8632-3331287a8759.JPG)

5.	Finding the top 5 sub-categories under the category Traffic.

![top5traffic](https://cloud.githubusercontent.com/assets/25045093/25310746/e63cbea8-27ba-11e7-8078-aabc84912135.JPG)

6.	Finding the emergency calls and the time of the day by categorizing as morning, noon, afternoon, evening and Night and finding their counts.

![timezone](https://cloud.githubusercontent.com/assets/25045093/25310747/f1159430-27ba-11e7-9017-16ff203ec530.JPG)

7.	It has been found that maximum emergencies lined up during the morning.
8.	Finding the counts of calls for each day of the week. Sunday has the lowest frequency of calls.

![day of the week](https://cloud.githubusercontent.com/assets/25045093/25310748/fa777a5c-27ba-11e7-8b7a-552c55633882.JPG)

9.	Finding the top 5 places from where 911 calls originated and their frequencies.

![top5twp](https://cloud.githubusercontent.com/assets/25045093/25310750/001f264e-27bb-11e7-98f4-97cc7c2f698b.JPG)

10.	Lower Merion seemed to be with most emergencies.
11.	Lower Merion seemed to be most affected by Traffic emergencies.
12.	Finding the Time zone of vehicle accidents at Lower Merion.

![lmaccidentstimezone](https://cloud.githubusercontent.com/assets/25045093/25310753/0bd950d6-27bb-11e7-8042-b3a7461b4081.JPG)

13.	The plot shows that vehicle accidents have occurred most during the morning and least in the night.
14.	Now, considering the 5 townships that made lowest number of 911 calls, Lehigh County was found to be the least.
![lowerplaces](https://cloud.githubusercontent.com/assets/25045093/25310758/28b09872-27bb-11e7-88a8-f70f6f74e4d1.JPG)


15.	Lehigh County has most emergencies as EMS. Now, finding the number of emergencies under each sub-category.

![lehighsubcat](https://cloud.githubusercontent.com/assets/25045093/25310757/2530f700-27bb-11e7-97fe-886de65abde1.JPG)

16.	Plotting the top 10 places for EMS Category.

![top10 ems](https://cloud.githubusercontent.com/assets/25045093/25310767/3a785bd0-27bb-11e7-96f9-9d06d72ef24c.JPG)


17.	Plotting the top 10 places for Fire Category.
![top10fire](https://cloud.githubusercontent.com/assets/25045093/25310765/3593e986-27bb-11e7-9fb4-aec0f0e533a5.JPG)

18.	Plotting the top 10 places for Traffic Category.

![top10traffic](https://cloud.githubusercontent.com/assets/25045093/25310768/3ef8ad90-27bb-11e7-93ee-5499b8ecb175.JPG)

19.	From this analysis, it has been found that Township Norristown has higher number of EMS, while low number of Fire and Traffic. Lower Merion has almost similar count for all categories.



  
