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

# ---- begin query ------#

# the beta query

# select total, errors, date, 100.0 * errors/total as percentage from
# (select count(status) as total,
# count(case when status !='200 OK' then status end) as errors,
# time::date as date
# from public.log
# group by time::date) order by time::date asc as errorSummary


# begin python code
import os
import psycopg2


error_analysis_query = "select date, 100.0 * errors/total as percentage from  \
                            (select count(status) as total,                                      \
                                count(case when status !='200 OK' then status end) as errors,    \
                                to_char(time::date, 'Mon,DD YYYY') as date from public.log group by time::date)          \
                            as errorSummary where (100.0 * errors/total) > 1.0 order by date asc"

popular_articles_query = \
    "select '\"' || articles.title || '\" ' || U&'\\2014' || ' ' || trim(to_char(count(articles.title), '999999')) || ' views' from log \
    full join articles on substring(path, character_length('/articles')+1, character_length(path)) = articles.slug \
    where log.path!='/' and log.status !='404 NOT FOUND' \
    group by articles.title order by count(articles.title) desc limit 3 "

popular_authors_query = "select authorname, count(authorname) from(select authors.name as authorname, slug from articles \
full join authors on author = authors.id) as authoredarticles                                                            \
right join log on substring(log.path, character_length('/articles')+1, character_length(log.path)) = slug                \
where log.path !='/' and log.status != '404 NOT FOUND' group by authorname order by count(authorname) desc"
results = []



def do_collection(dbname, host, user, password, port = ''):
    try:
        connection = psycopg2.connect(
                    dbname = dbname,
                    host = host,
                    user = user,
                    password =password,
                    port = port)
        cursor = connection.cursor()
        cursor.execute(popular_articles_query)
        results = cursor.fetchall()
        for result in results:
            #resultString = ' "{}" \u2104 {} views'.format(result)
            print(result)
        connection.close()
            
        
    except psycopg2.Error as error:
        print(error)
    except psycopg2.Warning as warning:
        print(warning)





if __name__ == "__main__":
    dbname = "news"
    host = "sql-node1.jtmorrisbytes.com"
    user = "web"
    password = "web"
    print("connecting to database {} as {} on {}"
          .format(dbname, user, host))

    do_collection(dbname, host, user, password)
    