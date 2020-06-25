During the setup process, you'll be asked to specify a default `username` and `password`. Select a username and password combination you'll remember since you're only installing PostgreSQL locally and don't need a highly secure combination.

Also during installation, you may be asked to specify a port number. Even though PostgreSQL will be running on the same machine, other applications communciate with it through the port as if it were on a remote machine. `Port number 5432` is the default for PostgreSQL.

Here are the installation instructions for each operating system:

`Mac`:

Download Postgres.app [here](https://postgresapp.com/), move to the Applications folder, and double click to launch. This applications runs in the background and you'll need it to be running to connect to it from Python. By default, PostgreSQL will run on port 5432.
Add the following line to the end of` ~/.bash_profile:
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin
Reset your terminal by executing source ~./bash_profile`

`Windows`:

Download the latest Windows installer [here], double click the installer, and go through the installation wizard.
When asked for a port number, use `5432`.

`Linux`:

Read the installation directions for your specific flavor of Linux from the official documentation.
If asked for a port number, use `5432`.
To test your installation, open your command line application, type `psql`, and you should be in the PostgreSQL shell.

To login with the username, simply type `psql -U (your username)`. For example, if you're trying to access the database under user "myuser", you would use the following psql login command: `psql -U myuser`. After you execute the command, enter the password, when prompted, to successfully connect to the desired database.

`psycopg2`

You can install this library using Anaconda:

`conda install psycopg2`

**Connecting to Postgres from psycopg2**

Launch your Python shell and import the psycopg2 library. Then, run the following code to connect to PostgreSQL and test that everything works as expected:
```
import psycopg2
conn = psycopg2.connect(dbname="postgres", user="postgres")
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("CREATE TABLE notes(id integer PRIMARY KEY, body text, title text)")
conn.close()
```
If no errors were returned, then you're setup is good to go!