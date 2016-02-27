#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from init import app

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__  == '__main__':
    app.run()
