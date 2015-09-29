Installation: 
=============

This blog runs in a virtual environment using virtualenv.  To  get vitualenv,
use the command:

    sudo pip install virtualenv

To create a virtual environment for this script, use the command:

    virtualenv venv

To activate that virtual environment, use the command:

    . venv/bin/activate

To install Flask from in the virtual environment, use the command:

    pip install Flask

To initialize the database, open an interactive python prompt (type 'python' in 
your virtualenv shell and hit enter) and run the following commands:

    from tcsblog import init_db
    init_db()

Exiting Virtualenv: 
===================

To exit that virtual environment, use the command:

    deactivate


