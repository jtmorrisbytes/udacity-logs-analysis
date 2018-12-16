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
import sys
import psycopg2


error_analysis_query = "select date || U&'\\2014' || ' ' || to_char(100.0 * errors/total, '0.00') || '% errors' as percentage from  \
                            (select count(status) as total,                                      \
                                count(case when status !='200 OK' then status end) as errors,    \
                                to_char(time::date, 'Mon,DD YYYY') as date from public.log group by time::date)          \
                            as errorSummary where (100.0 * errors/total) > 1.0 order by date asc"

popular_articles_query = \
    "select '\"' || articles.title || '\" ' || U&'\\2014' || ' ' || trim(to_char(count(articles.title), '999,999')) || ' views' from log \
    full join articles on substring(path, character_length('/articles')+1, character_length(path)) = articles.slug \
    where log.path!='/' and log.status !='404 NOT FOUND' \
    group by articles.title order by count(articles.title) desc limit 3 "

popular_authors_query = \
    "select authorname || ' ' ||  U&'\\2014' || ' ' || trim(to_char(count(authorname), '9,999,999'))|| ' views' \
    from    (select authors.name as authorname, slug from articles \
                full join authors on author = authors.id \
            ) as authoredarticles                                                            \
            right join log on substring(log.path, character_length('/articles')+1, character_length(log.path)) = slug   \
            where log.path !='/' and log.status != '404 NOT FOUND' group by authorname order by count(authorname) desc"
analysis_log = []

def results_to_array(cursor):
    query_result = cursor.fetchone()
    temp_array = []
    while query_result:
        if len(query_result) == 1:
            query_result = query_result[0]
        temp_array.append(query_result)
        query_result = cursor.fetchone()
    
    return temp_array

def write_log_file(input_array):
    log_file_string = ""
    for analysis_item_index in range(0, len(input_array)):
        analasis_item = input_array[analysis_item_index]
        title = analasis_item[0]
        content = analasis_item[1]
        log_file_string += "\t\t{}\n\n".format(title,)
        for item_index in range(0,len(content)):
            item = content[item_index]
            item_string = ""
            if analysis_item_index < 2:
                item_string = "\t{}. {}\n".format(item_index+1, item,)
            else:
                item_string = "\t*  {}\n".format(item,)
            log_file_string += "\t{}. {}\n".format(item_index+1, item,)
        #print(content)
    print(log_file_string)


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
        

        analysis_log.append(("Popular Articles", results_to_array(cursor)))
        connection.commit()
        cursor.execute(popular_authors_query)
        analysis_log.append(("Popular Authors", results_to_array(cursor)))
        connection.commit()
        cursor.execute(error_analysis_query)
        analysis_log.append(("Error Analasis Query", results_to_array(cursor)))
        connection.close()
        write_log_file(analysis_log)   
        
    except psycopg2.Error as error:
        print(error)
    except psycopg2.Warning as warning:
        print(warning)


if __name__ == "__main__":
    arguments = sys.argv
    print("arguments", arguments)
    
    for argument_index in range(1, len(arguments),):
        argument = arguments[argument_index]
        parameter = arguments[argument_index +1] 
        if argument == '--outfile':

    dbname = "news"
    host = "sql-node1.jtmorrisbytes.com"
    user = "web"
    password = "web"
    print("connecting to database {} as {} on {}"
          .format(dbname, user, host))

    do_collection(dbname, host, user, password)
    