# News Website Analysis
## By Jordan Morris


### This program is a Database log collection program designed to answer the three questions


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

#### minimum Requirements:
    Python 3, psycopg2, os.environ, os.path, getopt.getopt 


#### NOTICE: The program does NOT support SSL or ANY other form of encrypted communications. DO NOT expect any information to be transmitted in a secured form



* The program itself is really simple. it connects to the specified database with a username and password, then runs the analysis by running the queries, storing the result in memory, and then writing the result to a file.

* The program can be run on any host as long as the user uploads the newsdata.sql file or reproduces the tables inside newsdata.sql

##### The options are configured as followed:
    '-d': the name of the database
    '-u': the name of the database user
    '-h': the hostname or IP address of the database
    '-o': the path to output the log file
    "PASS=": An environment variable that holds the password

For security reasons, I have decided not to allow


