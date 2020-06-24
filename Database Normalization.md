There are are some drawbacks to storing the data which is not normalized:

- Data Duplication - we are storing the name of each wishlist multiple times.
- Data Modification - if we want to change the name of one of the wishlists, we have to modify multiple rows.
- Data Integrity - There is nothing to stop a row being added with the wrong wishlist name, and if

The process of optimizing the design of databases to minimize above issues is called **database normalization**. In database normalization theory, there are several different phases of normalization, known as normal forms.

Another table `wishlist_track` is now added to chinook database besides `wishlist` table (diagram in acccompanying jupyter note book). 

The `wishlist_track` table has two columns that are both yellow to indicate that they're `primary keys`, since neither column will uniquely identify each row by itself. When two or more columns combine to form a primary key it is called a `compound primary key`. To create a compound primary key, we use the PRIMARY KEY clause:
```
CREATE TABLE [table_name] (
    [column_one_name] [column_one_type],
    [column_two_name] [column_two_type],
    [column_three_name] [column_three_type],
    [column_four_name] [column_four_type],
    PRIMARY KEY (column_one_name, column_two_name)
);
```
Both columns in the wishlist_track table also have lines to indicate that they are `foreign keys`. To create a table with multiple foreign keys, we simply use multiple `FOREIGN KEY` clauses.

**Exercise**
Launch the SQLite shell, connected to the chinook.db database.
Create a new table, wishlist_track:
The table should have the following columns:
wishlist_id, with type INTEGER.
track_id, with type INTEGER.
A primary key should be specified, composed of both columns from the table.
Each of the columns should be designated as a foreign key as indicated in the schema diagram.
Quit the SQLite shell.

```
/home/pc$ sqlite3 chinook.db
#  sqlite3> CREATE TABLE wishlist_track (
#      ...> wishlist_id INTEGER,
#      ...> track_id INTEGER,
#      ...> PRIMARY KEY (wishlist_id, track_id),
#      ...> FOREIGN KEY (wishlist_id) REFERENCES wishlist(wishlist_id),
#      ...> FOREIGN KEY (track_id) REFERENCES track(track_id)
#      ...> );
#  sqlite3> .quit

```
```

