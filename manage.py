# _*_ coding: utf-8 _*_
__author__ = 'superman'
__date__ = '2018/3/26 14:08'
from app import app
import sys
import os
from flask_script import Manager

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, os.path.join(BASE_DIR, 'movie_project\\app'))
# sys.path.insert(0, os.path.join(BASE_DIR, 'movie_project\\app\\admin'))
# sys.path.insert(0, os.path.join(BASE_DIR, 'movie_project\\app\\home'))
# app.threaded = True
# manage = Manager(app)


if __name__ == "__main__":
    # manage.run()
    app.run(threaded=True)

