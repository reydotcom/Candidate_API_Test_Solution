This API was developed based on a technical assignment provided as a knowledge assessment to join the team. According to the task, the API should contain 5 functions:

    1.Return the time in Yerevan.
    2.Return a list of the top 10 largest cities in Armenia.
    3.Return information about Mount Ararat.
    4.Return a list of 5 famous Armenian dishes.
    5.Return a random word in Armenian.

Flask web framework was used as the foundation. PostgreSQL serves as the database, with SQLAlchemy library for database operations.

### How to run this code?

    1.Install and run PostgreSQL if you haven't done so before. Then create a database named `armenia`.

    2.Navigate to the directory where you want to place the project.
    2.1. Clone/unpack the project from GitHub.

    3.Execute the command `pip install -r requirements.txt`.

    4.Create a `.env` file and enter the data in the following format:
    DB_HOST=...
    DB_PORT=...
    DB_USER=...
    DB_PASS=...
    DB_NAME...

    5.Run the `starter.py` file with the command `python3 starter.py` and wait for it to finish creating tables in the database.

    6.Finally, you need to run the `app.py` file.
    6.1. Start by running the command `export FLASK_APP=app`.
    6.2. Now you can launch the project with the command `flask run`.
