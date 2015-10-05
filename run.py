#!venv/bin/python
import os


def main():
    # check that mail settings have been set in shell
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    MAIL = [MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD, MAIL_PASSWORD]    
    if None in MAIL:
        print "Please specify all MAIL settings in this shell before running run.py"
        return -1

    from app import app
    app.run(debug=False)

if __name__ == '__main__':
    main()
