# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 19:54:26 2017

@author: arzieg
"""

import logging

#create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handle and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')


