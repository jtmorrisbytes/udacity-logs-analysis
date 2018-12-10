#!/usr/bin/env python3
# logs_analysis.py
# this file to analyze the html logs


# database news
# tables: public.log


# task:
#
# On which days did more than 1% of requests lead to errors?
# The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.


# desired output format:
# july, 29, 2016 (em-dash)  2.5% errors


# the important columns in this question are status and time
# the staus column is stored as text
# the time column is stored as timestamp with the format "YYYY-MM-DD HH:MM:SS"
# the time column can be shortened to the
#     "YYYY-MM-DD format using 'time::date' in a select query"

# the algorytm:

# for each day,
# 1. count the number of requests made
# 2. count the number of requests that dont have
#    a "200 OK" status (errors)
#
# 3. if the ratio to number of errors to the number of requests is 1% or greater
#        a. convert the information to the desired format
#        b. append the information to a buffer or file (decide output format)
