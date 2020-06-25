#  Write a basic `select` query that will return all of the values from the `recent_grads` table, and **store this query as a string named query**.
# - use the `Cursor` method `execute()` to run the query against our database.
# - Return the full results set and store it as results.
# - Print the first three tuples in the list results.

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# SQL Query as a string
query = "select * from recent_grads;"
# Execute the query, convert the results to tuples, and store as a local variable
cursor.execute(query)
# Fetch the full results set as a list of tuples
results = cursor.fetchall()
# Display the first three results
print(results[0:3])





# Write a query that returns all of the values in the `Major` column from the `recent_grads table`.
# - Store the full results set (a list of tuples) in `majors`.
# - Then, `print` the first three tuples in majors

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# SQL Query as a string
query = "select Major from recent_grads;"
# Execute the query, convert the results to tuples, and store as a local variable
cursor.execute(query)
# Fetch the full results set as a list of tuples
majors = cursor.fetchall()
# Display the first three results
print(majors[0:3])

# Write and run a query that returns the `Major` and `Major_category` columns from recent_grads.
# Then, fetch the first five results and store them as `five_results`.

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query="select Major, Major_category from recent_grads"         
five_results=conn.execute(query).fetchmany(5)
print(five_results)


# Close the connection to the database using the Connection instance method `close()`

conn = sqlite3.connect("jobs.db")
conn.close()

# Write and execute a query that returns all of the `majors (Major)` in reverse alphabetical order (Z to A).
# Assign the full result set to `reverse_alphabetical`.
# Finally, close the connection to the database.

import sqlite3
conn2=sqlite3.connect("jobs2.db")
cursor=conn2.cursor()

query="select Major from recent_grads order by Major Desc;"
cursor.execute(query)
reverse_alphabetical=cursor.fetchall()
print(reverse_alphabetical[0:3])
conn2.close()

#  Write a basic `select` query that will return all of the values from the `recent_grads` table, and **store this query as a string named query**.
# - use the `Cursor` method `execute()` to run the query against our database.
# - Return the full results set and store it as results.
# - Print the first three tuples in the list results.

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# SQL Query as a string
query = "select * from recent_grads;"
# Execute the query, convert the results to tuples, and store as a local variable
cursor.execute(query)
# Fetch the full results set as a list of tuples
results = cursor.fetchall()
# Display the first three results
print(results[0:3])





# Write a query that returns all of the values in the `Major` column from the `recent_grads table`.
# - Store the full results set (a list of tuples) in `majors`.
# - Then, `print` the first three tuples in majors

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# SQL Query as a string
query = "select Major from recent_grads;"
# Execute the query, convert the results to tuples, and store as a local variable
cursor.execute(query)
# Fetch the full results set as a list of tuples
majors = cursor.fetchall()
# Display the first three results
print(majors[0:3])

# Write and run a query that returns the `Major` and `Major_category` columns from recent_grads.
# Then, fetch the first five results and store them as `five_results`.

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query="select Major, Major_category from recent_grads"         
five_results=conn.execute(query).fetchmany(5)
print(five_results)


# Close the connection to the database using the Connection instance method `close()`

conn = sqlite3.connect("jobs.db")
conn.close()

# Write and execute a query that returns all of the `majors (Major)` in reverse alphabetical order (Z to A).
# Assign the full result set to `reverse_alphabetical`.
# Finally, close the connection to the database.

import sqlite3
conn2=sqlite3.connect("jobs2.db")
cursor=conn2.cursor()

query="select Major from recent_grads order by Major Desc;"
cursor.execute(query)
reverse_alphabetical=cursor.fetchall()
print(reverse_alphabetical[0:3])
conn2.close()


