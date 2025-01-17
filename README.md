<img src="Python Bike.png" width="120" heigth="120" align="right" />

### 7 December 2019

# **Explore US Bike Share Data**

### Description
In this project, we use of Python to explore data related to bike share systems for three major cities in the United States — **Chicago**, **New York City** and **Washington DC** . The code import the data and answer interesting questions about it by computing descriptive statistics and takes in raw input to create an interactive experience in the terminal to present these statistics.

In this project, we use data provided by [Motivate](https://www.motivateco.com), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. The user is able to filter the information by city, month and weekday, in order to visualize statistics information related to a specific subset of data. The user is also able to choose to view raw data .

### What Software Do you Need ?
To complete this project, the following software requirements apply:
- You should have Python 3, NumPy, and pandas installed using [Anaconda](https://www.anaconda.com/distribution/)
- A text editor, like Sublime or Atom.
- A terminal application (Terminal on Mac and Linux or [Git Bash](https://git-scm.com/downloads) on Windows).

### Files used
The required files for running this program are:
- chicago.csv
- new_york_city.csv
- washington.csv

You can find these files [**Here**](https://drive.google.com/open?id=1EmZ8EJRjkU3EnQM6ntt9G5qVzZQSrHCo)

### The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g. , 776)
- Start Station (e.g. , Broadway & Barry Ave)
- End Station (e.g. , Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year

### Statistics Computed
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

##### 1. Popular times of travel (i.e., occurs most often in the start time)
- most common month
- most common day of week
- most common hour of day

##### 2. Popular stations and trip
- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

##### 3. Trip duration
- total travel time
- average travel time

##### 4. User info
- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

### An Interactive Experience

The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:
- Would you like to see data for Chicago, New York, or Washington?
- Would you like to filter the data by month, day, or not at all?
- (If they chose month) Which month - January, February, March, April, May, or June?
- (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.


### Credits
Useful Links you can refer to it:
- Python computing time periods : [Stackoverflow](https://stackoverflow.com/search?q=python+compute+time)
- Add Picture to README.md : [Stackoverflow](https://stackoverflow.com/questions/14675913/changing-image-size-in-markdown)
