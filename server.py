# -*- coding: utf-8 -*-

from app import *

if __name__ == '__main__':
    init()
    app.debug = True
    app.run(host='0.0.0.0')
