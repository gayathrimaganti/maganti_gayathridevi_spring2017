Data Analysis using Python : Midterm Exam Spring 2017

Question 1:

Enron Scandal Data Set: Analyzed Ken Lay's Documents who was the CEO and 
chairman of Enron Corporation for most of its existence and is a central figure 
in the Enron scandal.

Analysis 1 & 2:
1. Stored the enron dataset in a relative path of "../midterm/data/enron/" that 
contains email content of some important employees of Enron.

2. Printing Ken Lay's folders & Finding the number of files in each of the folders
by iterating through the directories, subdirectories etc and finding the count of the files
present.
![number of folders and files](https://cloud.githubusercontent.com/assets/25045093/25073796/3187b1be-22bc-11e7-9ee0-9896c4808d90.JPG)

3. Reading the first document of the all_documents folder, by using the email parser library
i.e., to read the main part of the email.

4. Finding the to-emails list and from-emails list sent to-and-from Ken Lay 
along with the body of the emails using a function that takes file as input and the empty lists 
into which the data can be written and then, saving the data as .txt files.

5. Finding the top 100 most common words used in the body of the emails of Ken Lay's inbox 
folder by using the body.txt file that was generated. Also, removing the unwanted characters 
using regular expressions and finding the common words used and their frequency distribution 
using NLTK and printing them.
![100 most frequent words](https://cloud.githubusercontent.com/assets/25045093/25073801/5093f112-22bc-11e7-8d54-9eaaf1866452.JPG)


6. Finding the top 10 most common to-email addresses and from-email addresses that were 
commonly used out of the entire Enron email Dataset.
![10 most common email adreses](https://cloud.githubusercontent.com/assets/25045093/25073804/59dbd000-22bc-11e7-89c8-af0398a1cb02.JPG)


Analysis 3:

1. Storing the emails.csv file in the data folder and accessing this file to analyze the emails using 
pandas.
2.Filtered only those files that contain the word 'sent' in their file names.
3. Using this list to find the top ten email senders.
![top 10 senders pandas](https://cloud.githubusercontent.com/assets/25045093/25073807/73942b50-22bc-11e7-985a-94db85c8ed0c.JPG)

4.Defining two functions, get_text_from_email & split_email_addresses to get content from 
emails and to separate multiple email addresses.
5. Parsing the emails into a list of email objects and then parsing the content from emails.
6. Finding the shape of the Dataframe and the number of unique values in each of the columns.
![shape of the dataframe](https://cloud.githubusercontent.com/assets/25045093/25073808/7abdbb80-22bc-11e7-83e7-492ec3822c09.JPG)

7. After parsing the date, using this data to find the number of emails sent across the years,
day of the week and hour. 
![n and year](https://cloud.githubusercontent.com/assets/25045093/25073810/7fd3c614-22bc-11e7-9315-8e4e51b90ccf.JPG)
![n and day of the week](https://cloud.githubusercontent.com/assets/25045093/25073812/8419df06-22bc-11e7-9008-6b9334a70159.JPG)
![n and hour](https://cloud.githubusercontent.com/assets/25045093/25073813/88477822-22bc-11e7-8e8a-e9f4683b21f4.JPG)

Question 2:

Analysis 1:
1. Collected the data in json format from NYT Archive API using the API Key and requests library,
i.e, by iterating over the archive of upto 120 pages.
2. Hid the api key as an enivornment variable in the OS.
3. Stored the data in the ArchiveData folder with the name Archive(i) given to each of the files.
4. Reading the files in the specified path and storing it in a variable 'data'.
5. Storing values of the keys 'response', 'docs' in the response_data variable.
6. Creating an empty dictionary to read every new section name and append it to an empty list without 
repetitions.
7. Printing  Top 20 sections that appeared.
![1](https://cloud.githubusercontent.com/assets/25045093/25073847/3eb8fb1c-22bd-11e7-8551-95f618d728dd.JPG)

8. Creating an empty dictionary to hold the articles and their article count values, looping through the 
sections for articlecounts of the particular article in the archive.
9. Printing the dictionary of Articles and their values.
![2](https://cloud.githubusercontent.com/assets/25045093/25073850/4623f352-22bd-11e7-8b7c-42815ddbe8a8.JPG)

10. Sorting the articles according to their articlecounts and printing the top 40 sections.
![3](https://cloud.githubusercontent.com/assets/25045093/25073852/4a8fc60a-22bd-11e7-96ab-f634e843677e.JPG)

11. Plotting a bar graph using Matplotlib for Articles and their articlecount values.
![4](https://cloud.githubusercontent.com/assets/25045093/25073854/4e3e9bfa-22bd-11e7-81e9-24ee2a9e6765.JPG)



Analysis 2 & 3:
1. 1. Collected the data in json format from NYT Archive API using the API Key and requests library,
i.e, by iterating over the archive of upto 120 pages.
2. Hid the api key as an environment variable in the OS.
3. Stored the data in the ArticleSearch folder with the name Article(i) given to each of the files.
4. Finding the number of files under each section and printing them.
![5](https://cloud.githubusercontent.com/assets/25045093/25073892/301327d0-22be-11e7-925c-c296f7a6c1aa.JPG)

5. Finding the Sections and Sub-sections present under each section and printing them.
![6](https://cloud.githubusercontent.com/assets/25045093/25073896/453b98fe-22be-11e7-9f80-e4591cf39153.JPG)

6. As Sports section contains many subsections, we can analyze if further.
7. Finding the number of articles present in each subsection of the Sports Section.
![7](https://cloud.githubusercontent.com/assets/25045093/25073901/4c8e1f8c-22be-11e7-9c90-628f4200641a.JPG)

8. As Soccer has the most number of articles, we check for the word soccer in each of the headlines and 
append it to a list to form a single text. 
9. Removing all the unwanted characters and numbers from the text, filtering the headlines text to give data without stop words.
10. Finding the 100 most common words and displaying them. 

![8](https://cloud.githubusercontent.com/assets/25045093/25073902/556a8b90-22be-11e7-8180-dec74bb79e96.JPG)
