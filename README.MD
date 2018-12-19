# News Website Analysis
## By Jordan Morris


### This program is a Database log collection program designed to answer three questions from the Udacity Nanodegree project

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

    1. "Princess Shellfish Marries Prince Handsome" — 1201 views
    2. "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
    3. "Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

    1. Ursula La Multa — 2304 views
    2. Rudolf von Treppenwitz — 1985 views
    3. Markoff Chaney — 1723 views
    4. Anonymous Contributor — 1023 views
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Example:

* July 29, 2016 — 2.5% errors

### The program:

#### Minimum Requirements:
    Python 3, psycopg2, os.environ, os.path, getopt.getopt 


#### NOTICE: The program does NOT support SSL or ANY other form of encrypted communications. DO NOT expect any information to be transmitted in a secured form



* The program itself is really simple. it connects to the specified database with a username and password, then runs the analysis by running the queries, storing the result in memory, and then writing the result to a file.

* The demo ~~can be run on any host as long as the user uploads the newsdata.sql file or reproduces the tables inside newsdata.sql~~ can currently only be run if the user accesses my database or has access to newsdata.sql that contains the demo information

* When the program is not given any options, It will default to hardcoded values used in the demo. When an output path is not specified, the program will drop "news_log_analysis.txt" in the current directory derived from expanding the "." operator


##### The options are configured as followed:
    '-d': the name of the database
    '-u': the name of the database user
    '-h': the hostname or IP address of the database
    '-o': the path to output the log file
    "PASS=": An environment variable that holds the password

For security reasons, I have decided not to allow the password to be included as a command line argument.


## The demo:

To run the demo, please do the following:

1. Ensure that you are connected to the internet
2. Install python 3 from https://www.python.org/ for your operating system
3. Clone the github repo or download the zip file and extract it.
4. Open a terminal window pointing to the location of the github project
5. Install the requirements by running <code>pip3 -r requirements.txt </code>
5. Run "news_log_analysis.py" or "python3 news_log_analysis.py" without any options.
6. The program should connect to my database, run the analysis, and drop a text file answering the above questions.

# Problems?
Please submit a github issue or contact me at <a href="mailto:jthecybertinkerer@gmail.com?subject=news%20log%20analysis%20issue">jthecybertinkerer@gmail.com</a> with a report of what went wrong, what you expected to happen, and what steps you did to reproduce the problem. I will do my best to get back to you as soon as possible.


