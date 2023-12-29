# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import mlflow

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

def print_hi():

    uri='mysql://user:password@localhost:3306/database_name'
    exp_name='mysql-as-backend-and-local-artifact'
    run_name='1'

    mlflow.set_tracking_uri(uri)
    mlflow.set_experiment(exp_name)
    mlflow.start_run(run_name=run_name)
    mlflow.sklearn.autolog()

    db = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

    # Create and train models.
    rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
    rf.fit(X_train, y_train)

    # Use the model to make predictions on the test dataset.
    predictions = rf.predict(X_test)
    print("Done")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
