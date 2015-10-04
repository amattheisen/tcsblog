Inspiration:
============
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-now-with-python-3-support

Installation: 
=============

This blog runs in a virtual environment using virtualenv.  To  get vitualenv,
use the command:

    sudo pip install virtualenv

To create a virtual environment for this script, use the command:

    virtualenv.py venv

To activate that virtual environment, use the command:

    . venv/bin/activate

To install Flask from in the virtual environment, use the command:

    pip install Flask
    pip install Flask-SQLAlchemy
    ...

To initialize the database, open an interactive python prompt (type 'python' in 
your virtualenv shell and hit enter) and run the following commands:

    from ablog import db
    db.create_all()

Exiting Virtualenv: 
===================

To exit that virtual environment, use the command:

    deactivate


Useful Docs
===========
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-full-text-search
http://markdownlivepreview.com
https://pythonhosted.org/Flask-WhooshAlchemy/
http://getbootstrap.com
http://momentjs.com
https://github.com/scrooloose/nerdtree
https://github.com/nathanaelkane/vim-indent-guides

