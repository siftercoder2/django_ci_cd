from django.http import HttpResponse
import logging 
logger = logging.getLogger(__name__)
from random import randrange


def index(request):
	levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
	num = randrange(len(levels))

	if num == 0:
		logger.debug("This is a debug")	
	elif num == 1:	
		logger.info("This is a info")	
	elif num == 2:
		logger.warn("This is a warning")		
	elif num == 3:
		logger.error("This is an error")
	elif num == 4:
		logger.critical("This is an critical")					

	return HttpResponse("Hello, world. You're at the polls index app")