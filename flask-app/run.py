"""
Description: Script for starting the flask application. Usage: $ python run.py
"""
from library_app import app


# If you want some code to not be executed when this file is imported, but only
# when this file is run as "python filename.py", then put it under __name__=='__main__'.
# More about this here: https://stackoverflow.com/a/419185
if __name__ == '__main__':
    app.run(debug=True)
