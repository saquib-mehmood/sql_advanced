A primary key is a unique identifier for each row - we cannot have two rows in a table with the same value for the `primary key` column(s).

When two tables have a relation, there will be a column in one table that is a primary key in another table. This is known as a `foreign key`. By defining a `foreign key`, our database engine will prevent us from adding rows where the `foreign key` value doesn't exist in the other table, which helps to prevent errors in our data.

Usually, a `primary key` is specified as part of a create statement. Once the `primary key` is defined, the database engine will prevent any new rows from being added to the database if they have the same primary key as any existing rows. 

By adding a `FOREIGN KEY` clause, we can define one of our columns as a foreign key and specify the table and column that it references.

```
CREATE TABLE user (
    user_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);

```
e.g for creating a table 'spill':

```
CREATE TABLE spill (
   spill_id INTEGER PRIMARY KEY,
    loc_id INTEGER,
    spill_date TEXT,
    total NUMERIC,
    FOREIGN KEY (locl_id) REFERENCES loc(loc_id)
);

```
We will create `tables`, `primary key`s and `foreign keys` to add new tables to `Chinook` database that allow customers to create "wishlists" of tracks they would like to buy (image in accompanying jupyter notebook).

**Exercise**
Launch the SQLite shell (or jupyter notebook) , connected to the chinook.db database.
Create a new table, wishlist, with the following columns:
wishlist_id, with type INTEGER.
This column should be the primary key.
customer_id, with type INTEGER.
This column should have a foreign key relationship with the customer_id column from the customer table.
name, with type TEXT.
Quit the SQLite shell.

```
/home/pc$ sqlite3 chinook.db
#  sqlite3> CREATE TABLE wishlist (
#      ...> wishlist_id INTEGER PRIMARY KEY,
#      ...> customer_id INTEGER,
#      ...> name TEXT,
#      ...> FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
#      ...> );
#  sqlite3> .quit

```

