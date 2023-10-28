import pandas as pd
from flask import Flask
from sqlalchemy import create_engine


app = Flask(__name__)




# #@app.route('/hello')
# def hello_world():
#     return 'Hello, World!'

@app.route('/retrieve')

def retrieve():

    
    my_conn = create_engine("mysql+mysqlconnector://root:root123!@localhost:3306/testdb", echo=True).connect()
    read_file = pd.read_sql_query('SELECT * FROM testdb.employee', my_conn)
    #normal_file = read_file_json('data.json', orient='records')
    read_file = read_file.to_json()
    return read_file

    
if __name__ == '__main__':
    app.run(debug=True)