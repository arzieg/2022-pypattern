# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:01:45 2017

@author: arzieg
"""
# Beispiel mit einer logging.conf Datei

import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger(__name__)


# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

