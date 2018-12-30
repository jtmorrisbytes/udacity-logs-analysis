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

* The demo can only be run inside of Udacity's Vagrant VM if used without command line arguments.

* When the program is not given any options, It will default to connecting to the database news on the default connection socket using the curently logged in user with no password. When an output path is not specified, the program will drop "news_log_analysis.txt" in the current directory derived from expanding the "." operator


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
2. Install Virtualbox and Vagrant
3. Download  and extract the github repository at https://github.com/udacity/fullstack-nanodegree-vm.git
4. Open a terminal window and go to the vagrant file at (project-root)->vagrant
5. Clone the udacity_logs_analysis project inside the vagrant directory
6. Run the command <code>vagrant up</code> on the directory containing the vagrantfile and wait for the VM to boot
7. Once booted use <code>vagrant ssh </code> to ssh into the virtual machine
8. Locate the udacity_logs_analysis folder inside the /vagrant directory
9. Install the requirements by <code>sudo pip3 install psycopg2 </code>

10. Run "news_log_analysis.py" or "python3 news_log_analysis.py" without any options.
11. The program should connect to the vagrant vm's database, run the analysis, and drop a text file int the current working directory containing the results.

# FAQ
* If the database connection times out, make sure you reprovision the VM with <code>vagrant provision</code> using the terminal window you used to start the VM and try again
* If you get the error <code>Import Error, no such library "psycopg2"</code> make sure that you are connected to the internet and ran the command in step 9.

# Problems?
Please submit a github issue or contact me at <a href="mailto:jthecybertinkerer@gmail.com?subject=news%20log%20analysis%20issue">jthecybertinkerer@gmail.com</a> with a report of what went wrong, what you expected to happen, and what steps you did to reproduce the problem. I will do my best to get back to you as soon as possible.


