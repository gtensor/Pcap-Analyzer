# coding:UTF-8
from flask import Flask

app = Flask(__name__)

app.config.from_object('config')
# 导入函数到模板中
app.jinja_env.globals['enumerate'] = enumerate

# import views
from pcapalyzer import views
