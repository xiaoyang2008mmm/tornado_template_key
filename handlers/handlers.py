# -*- coding: utf-8 -*- 
from views.views import *
import os.path

STATIC_PATH   = os.path.join(os.path.dirname(__file__), "../static")
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "../templates")
HANDLERS =[(r"/" ,Index_Handler),
	]
#自定义ui模块函数
ui_modules={'Hello': HelloModule}
