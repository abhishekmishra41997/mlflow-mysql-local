# mlflow-mysql-local

Note: Mysql must be installed on system
1. Open terminal
2. Clone this repository with command
```git clone https://github.com/abhishekmishra41997/mlflow-mysql-local.git```
3. Install required packages with
4. ```pip install -r requirements.txt```
5. login to mysql server and create database with below query for mlflow
```CREATE DATABASE Database_name;```
6. Create schema for mlflow tracking data storage with below command (Replace user and password with your credential in below command)
```mlflow db upgrade mysql://username:password@localhost:3306/database_name```
7. Now, run mlflow - server with below command
```mlflow server --backend-store-uri mysql://username:password@localhost:3306/database_name```
8. Now, you will be able to see mlflow ui on 5000 port.
9. Set the uri, exp_name and run_name variable in main.py file.
10. Run the main.py file.
11. Once main.py finish, go to mlflow ui, you'll be able to see experiments and run.