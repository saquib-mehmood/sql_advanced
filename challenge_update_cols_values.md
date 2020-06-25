**Scenario**

Up until now, the Chinook store hasn't had to collect sales tax, but due to some new tax legislation, we will need to charge customers in certain countries taxes on their purchases.
We need to add the following columns to the `invoice table`:

`subtotal`
`tax`

We also need to update all existing invoices with data for these two new columns. The value for the `tax` column will need to be `0` for every row, and the value for the `subtotal` column will need to be the **same as the total column for each row**.

the first five rows of those columns will need to look like following:
```
sqlite> SELECT
   ...>    invoice_id,
   ...>    subtotal,
   ...>    tax,
   ...>    total
   ...> FROM invoice
   ...> LIMIT 5;
invoice_id  subtotal    tax         total
----------------------
1           15.84       0           15.84
2           9.9         0           9.9
3           1.98        0           1.98
4           7.92        0           7.92
5           16.83       0           16.83
```
**Requirement**
Launch the SQLite shell, connected to the `chinook.db` database.
Add two new columns, with values, to the invoice table:
- `tax`, with type `NUMERIC`.
The value for all existing rows should be 0.
- `subtotal`, with type `NUMERIC`.
The value for each row should be the same as that row's value for total.
Quit the SQLite shell.

```
/home/pc$ sqlite3 chinook.db
#  sqlite3> ALTER TABLE invoice
#      ...> ADD COLUMN tax NUMERIC;
#  sqlite3> ALTER TABLE invoice
#      ...> ADD COLUMN subtotal NUMERIC;
#  sqlite3> UPDATE invoice
#      ...> SET
#      ...>     tax = 0,
#      ...>     subtotal = total;
#  sqlite3> .quit
#
```