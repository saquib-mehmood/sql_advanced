IF a customer wants to remove a track from their wishlist, One might just `DELETE` the row from wishlist_track. 
But we will not retain any historical data on which tracks were added to wishlists which reduces our ability to analyze this in the future.

A better approach would be to add a column that has a `boolean` value to show whether the row is active or not, and just change that value if the user wants to delete a track. We can do a similar thing with the wishlists themselves, so users can delete (or technically, deactivate) wishlists they no longer want to use.

We'll need to add a column to each of our tables. We can use the `ALTER` statement to do this.

```
ALTER TABLE [table_name]
ADD COLUMN [column_name] [column_type];

```
SQLite supports only five basic types of data - the closest thing to a `boolean` type is `NUMERIC`, where the values 1 and 0 will represent true and false respectively.

**Exercose**
Launch the SQLite shell, connected to the `chinook.db` database.
Create a new column, `active`, in the wishlist table with type `NUMERIC`.
Create a new column, `active`, in the `wishlist_track` table with type NUMERIC.
Quit the SQLite shell.

```
home/dq$ sqlite3 chinook.db
#  sqlite3> ALTER TABLE wishlist
#      ...> ADD COLUMN active NUMERIC;
#  sqlite3> ALTER TABLE wishlist_track
#      ...> ADD COLUMN active NUMERIC;
#  sqlite3> .quit
```