Launch the `SQLite shell`, connecting to the `chinook.db` database file.
Use `.tables` to display the tables in the Chinook database.
Use dot commands to turn headers on, and set the mode to 'column'.
Write a query on one of the tables in the chinook.db database.
Display the help text.
Run .shell clear to see what it does.
Quit the SQLite shell.

```
 
# /home/pc$ sqlite3 chinook.db
#  sqlite3> .tables
#  sqlite3> .headers on
#  sqlite3> .mode column
#  sqlite3> SELECT
#      ...>   track_id,
#      ...>   name,
#      ...>   album_id
#      ...> FROM track
#      ...> WHERE album_id = 3;
#  sqlite3> .help
#  sqlite3> .shell clear
#  sqlite3> .quit

```