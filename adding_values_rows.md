To change values for existing rows, we use the `UPDATE` statement:
```
UPDATE [table_name]
SET [column_name] = [expression]
WHERE [expression]
```

The `WHERE` clause is optional, and can contain any expression that would be valid in a `SELECT` statement.
There are several variations we can use for our `SET` clause. First we can use a single value:
```
UPDATE customer
SET phone = "+55 (12) 3921-4464"
WHERE customer_id = 1
```
We can use a `subquery`that returns a single value:
```
UPDATE track
SET unit_price = (
                    SELECT AVG(unit_price)
                    FROM track
                 )
```
We can use a column, or function on an existing column:
```
UPDATE track
SET unit_price = unit_price * 1.1
```
We can also set more than one column at once:
```
UPDATE wishlist_track
SET
    active = 1,
    purchased = 0;
```
Because our active columns will store a `1` for `true` and `0` for `false`, we'll set the values to `1` for every row.

**Exercise**
Launch the SQLite shell, connected to the `chinook.db` database.
Set all values for the `active` column in the `wishlist table` to `1`.
Set all values for the `active` column in the `wishlist_track` table to `1`.
Quit the SQLite shell.

```
