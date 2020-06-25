# Enter and quit psql tool
psql 
\q

# Running sql queries
psql
CREATE DATABASE bank_accounts;
\q

# special psql commands

psql
\l
\q

# switching Databases
psql -d bank_accounts
CREATE TABLE deposits (id integer PRIMARY KEY, name text, amount float);

# creating users
psql
CREATE ROLE sec WITH CREATEDB LOGIN PASSWORD 'test';
 
# adding permissions
psql -d bank_accounts
GRANT ALL PRIVILEGES ON deposits TO sec;
\dp deposits

# removing permissions

psql -d bank_accounts
REVOKE ALL PRIVILEGES ON deposits TO sec;
\dp deposits

# superuser

psql
CREATE ROLE aig WITH LOGIN PASSWORD 'test' SUPERUSER;
\du