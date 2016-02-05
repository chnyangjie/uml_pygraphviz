# coding=utf-8
'''
Created on Feb 4, 2016

@author: yangjie
'''
import logging
formatStr = "%(asctime)s [%(filename)s line %(lineno)d] [%(name)s %(levelname)s] %(message)s"
fmt = logging.Formatter(formatStr)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(fmt)

uml_logger = logging.getLogger("UML_LOGGER")
uml_logger.setLevel(logging.INFO)
uml_logger.addHandler(streamHandler)