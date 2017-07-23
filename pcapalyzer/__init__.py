# coding:UTF-8
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config.from_object('config')
# 导入函数到模板中
app.jinja_env.globals['enumerate'] = enumerate

toolbar = DebugToolbarExtension()
toolbar.init_app(app)
# import views
from pcapalyzer import views
