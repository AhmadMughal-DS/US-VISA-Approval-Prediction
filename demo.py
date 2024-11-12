"""
# this si demo of logging file in us visa project
from US_VISA.logger import logging
logging.info("Welcome to US VISA project")
"""




from US_VISA.exceptions import USVISAException
import sys


try:
    a = 2/0
except Exception as e:    
    raise USVISAException(e,)



