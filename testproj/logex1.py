# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:22:15 2017

@author: arzieg
"""

import logging
import sys


# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug
loglevel=sys.argv[1]
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level,int):
    raise ValueError('Invalid log level: %s' %loglevel)
# log to file
#logging.basicConfig(filename='C:/Users/arzieg/workspace/python/example.log', level=numeric_level)
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')

#log to console and file
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', 
                    level=numeric_level,
                    datefmt='%d-%m-%Y: %H:%M:%S ')
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
