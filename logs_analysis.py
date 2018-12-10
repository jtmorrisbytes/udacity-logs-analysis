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



#SQL exploration

# count all records:with status entries: select count(status) from public.log 
# count all records that produced an error : select count(*) from public.log where status != '200 OK'


# query in progress
# select count(status) as totalRequests, (select count(status) from public.log where status != '200 OK') as errors from public.log



# begin python code
import os
import psycopg2


class public_log:
    # the web page path type text, nullable
    path = ""
    # the ip address that was logged
    ip = ""
    # the response from the server
    status = ""
    # the timestamp in "YYYY-MM-DD HH:MM:SS" format
    timestamp = ""
    # the primary key, 
    id = 0

    def do_collection(self, dbname, host, user, password, port):
        try:
            connection = psycopg2.connect(
                        dbname=dbname,
                        host=host,
                        user=user,
                        password=password,
                        port=port)
            cursor = connection.cursor()
            cursor.execute("select path, status, time from public.log where status != '200 OK' order by time asc limit 100")
            result = cursor.fetchone()
            while result:
                if(result):
                    print(result)
                result = cursor.fetchone()
            connection.close()
        except psycopg2.Error as error:
            print(error)
        except psycopg2.Warning as warning:
            print(warning)

if __name__ == "__main__":
    dbname = "news"
    host = os.environ.get("HOST", "127.0.0.1")
    port = os.environ.get("PORT")
    user = os.environ.get("PSQLUSER")
    password = os.environ.get("PASS")
    print("connecting to database {} as {} on {} using port {}"
          .format(dbname, user, host, port))

    public_log().do_collection(dbname, host, user, password, port)