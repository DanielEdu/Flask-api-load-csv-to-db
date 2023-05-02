
# Flask App with Postgres and Docker

This is a simple Flask application that uses Postgres as the database and can be run inside a Docker container.

## Requirements

* Docker
* Docker Compose

## Setup

1. Clone this repository to your local machine.

2. Navigate to the project directory.

3. Run the following command to start the application: `docker-compose up`

4. Open a web browser and navigate to `http://localhost:5000` to access the web application.

Configuration
Before running the program, you must configure the following environment variables:

POSTGRES_USER: PostgreSQL database user.
POSTGRES_PASSWORD: Password for the PostgreSQL database user.
POSTGRES_DB: Name of the PostgreSQL database to use.
FLASK_APP: Name of the Flask application file.
FLASK_ENV: Execution mode of the application (development, production, etc).
To configure these environment variables, you can create a file named .env in the root directory of the project and set the values accordingly. For example

```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=mydatabase
FLASK_APP=app.py
FLASK_ENV=development
```

Then, when running the application with Docker, you can use the --env-file option to load the environment variables from the .env file. For example:

```docker
docker run --env-file .env my-flask-app
```

Alternatively, you can set the environment variables directly in the command line when running the Docker container. For example:

```docker
docker run -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=mydatabase -e FLASK_APP=app.py -e FLASK_ENV=development my-flask-app
```

## Usage

The application provides the following functionality:

* **Upload CSV data**: You can upload data to the 'hired_employees', 'departments', and 'jobs' tables in your database by clicking on the 'Upload' link in the navigation bar.

* **Quarterly employee report**: You can view a report of the number of employees hired by quarter and department by clicking on the 'Quarterly Report' link in the navigation bar.

* **Employee job report**: You can view a report of the number of employees hired by job and department by clicking on the 'Job Report' link in the navigation bar.

## Cleaning up

To stop the application and remove the Docker container, use the following command:

```docker-compose down```

This will stop the application and remove the container, but it will retain the database data in a Docker volume.


## To host your Flask app on AWS, you can follow these general steps

1. **Create an EC2 instance:** Log in to the AWS Management Console and create a new EC2 instance. Choose an Amazon Machine Image (AMI) that fits your requirements and select the instance type that you want to use. Make sure to configure your security group to allow inbound traffic on the appropriate ports (usually 80 for HTTP and 443 for HTTPS).

2. **Install the required dependencies:** Once your instance is up and running, log in to it and install the necessary dependencies for your Flask app. This may include packages like Python, pip, and virtualenv.

3. **Upload your Flask app code:** Copy your Flask app code to the EC2 instance. You can use git to clone your repository or copy your files using scp or rsync.

4. **Configure your Flask app:** Set the necessary environment variables for your Flask app, such as the database connection string, secret key, and other configuration parameters. You can set these environment variables in a .env file or by using the export command.

5. **Install and configure a web server:** To serve your Flask app, you will need to install and configure a web server like Apache or Nginx. Configure the web server to act as a reverse proxy for your Flask app, so that incoming HTTP requests are forwarded to your Flask app running on a specified port.

6. **Start your Flask app:** Activate your virtual environment and start your Flask app by running the appropriate command (e.g., flask run or gunicorn app:app). Make sure that your Flask app is running and accessible through the web server.

7. **Set up a domain name:** Optionally, you can set up a domain name for your Flask app using Amazon Route 53 or another DNS service. This will allow you to access your Flask app using a custom domain name.

These are the general steps to host your Flask app on AWS. There may be additional steps depending on your specific use case and requirements.

## To create a PostgreSQL database on AWS, you can follow these general steps

1. Sign in to the AWS Management Console and open the Amazon RDS console.

2. Click on "Create database" and select "PostgreSQL".

3. Choose the appropriate version of PostgreSQL and specify the database settings, such as the database name, username, and password.

4. Select the instance type, storage type, and size.

5. Configure the VPC, subnet group, and security group settings.

6. Review your settings and click "Create database" to launch the instance.

7. Wait for the database instance to be created and then connect to it using a PostgreSQL client such as pgAdmin.

8. Create the necessary tables and set up the schema for your Flask app using SQL commands.

Note: These steps are a general guideline and may differ slightly depending on the specific AWS services you are using and your individual configuration needs. Be sure to follow AWS documentation and best practices for optimal results.
