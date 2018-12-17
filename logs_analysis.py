#!/usr/bin/env python3
# logs_analysis.py
# this file to analyze the html logs


# database news
#
# task:
#
# On which days did more than 1% of requests lead to errors?
# The log table includes a column status that indicates the HTTP status code
# that the news site sent to the user's browser.


# desired output format:
# july, 29, 2016 (em-dash)  2.5% errors
# begin python code
import os
import sys
import psycopg2

# globals
outputpath = os.path.abspath(os.path.join(".", "news_log_analysis.txt"))
dbname = "news"
host = "sql-node1.jtmorrisbytes.com"
user = "web"
password = "web"


error_analysis_query = \
    "select date || ' ' || U&'\\2014' || ' ' ||\
    to_char(100.0 * errors/total, '0.00') || '% errors' as percentage from\
        (select count(status) as total,\
        count(case when status !='200 OK' then status end) as errors,\
        to_char(time::date, 'Mon,DD YYYY') as date \
        from public.log group by time::date)\
    as errorSummary where (100.0 * errors/total) > 1.0 order by date asc"

popular_articles_query = \
    "select '\"' || articles.title || '\" ' || U&'\\2014' || ' '\
    || trim(to_char(count(articles.title), '999,999')) || ' views' from log\
    full join articles on substring(path, character_length('/articles')+1, \
                          character_length(path)) = articles.slug\
    where log.path!='/' and log.status !='404 NOT FOUND'\
    group by articles.title order by count(articles.title) desc limit 3 "

popular_authors_query = \
    "select authorname || ' ' ||  U&'\\2014' || ' ' ||\
     trim(to_char(count(authorname), '9,999,999'))|| ' views'\
     from    (select authors.name as authorname, slug from articles\
                full join authors on author = authors.id\
            ) as authoredarticles\
            right join log on \
            substring(log.path, character_length('/articles')+1,\
            character_length(log.path)) = slug\
            where log.path !='/' and log.status != '404 NOT FOUND' \
            group by authorname order by count(authorname) desc"
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
    log_file_string = \
    "\t\tNews Log Analysis:\n\
    This log is generated as a result of an udacity project\n\
    see the source code  and more details at\n\
    https://github.com/jtmorrisbytes/udacity-logs-analysis/\
    blob/master/README.MD\n\n \
    This log is a summary of the following components:\n\
    \tA. Of all articles in the news database,\n\
    \t   which three are the most popular?\n\
    \tB. How popular are the article authors in order\n\
    \t   from most to least popular?,\n\
    \tC. On which days did visiting the website resulted in the server\n\
    \t   returning errors on more than 1% of visits?\n\
    ------------------------BEGIN LOG--------------------------\n\n\
    "
    for analysis_item_index in range(0, len(input_array)):
        analasis_item = input_array[analysis_item_index]
        title = analasis_item[0]
        content = analasis_item[1]
        log_file_string += "\t\t\t{}\n\n".format(title,)
        for item_index in range(0, len(content)):
            item = content[item_index]
            item_string = ""
            if analysis_item_index < 2:
                item_string = "\t{}. {}\n".format(item_index+1, item,)
            else:
                item_string = "\t*  {}\n".format(item,)
            log_file_string += "\t{}. {}\n".format(item_index+1, item,)
        if analysis_item_index < len(input_array) - 1:
            log_file_string += "\n\n"
    log_file_string += \
        "------------------------END LOG--------------------------\n"
    try:
        log_file = open(outputpath, 'w', encoding="utf-8")
        log_file.write(log_file_string)
        log_file.close()
        print("wrote log file to \"" + outputpath + "\"")
    except FileNotFoundError as notFoundError:
        print(notFoundError)


def do_collection(dbname, host, user, password, port=''):
    try:
        connection = psycopg2.connect(
                    dbname=dbname,
                    host=host,
                    user=user,
                    password=password,
                    port=port)
        cursor = connection.cursor()
        print("running analysis on database")
        cursor.execute(popular_articles_query)
        analysis_log.append(("Popular Articles", results_to_array(cursor)))
        connection.commit()
        cursor.execute(popular_authors_query)
        analysis_log.append(("Popular Authors", results_to_array(cursor)))
        connection.commit()
        cursor.execute(error_analysis_query)
        analysis_log.append(("Error Analasis Query", results_to_array(cursor)))
        connection.close()
        print("analysis complete")
        write_log_file(analysis_log)
    except psycopg2.Error as error:
        print(error)
    except psycopg2.Warning as warning:
        print(warning)


if __name__ == "__main__":
    print("connecting to database {} as {} on {}"
          .format(dbname, user, host))
    do_collection(dbname, host, user, password)
