# -*- coding: utf-8 -*-

from app import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    init()
    app.run(host='0.0.0.0')
