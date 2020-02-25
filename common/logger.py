import logging.handlers

logger = logging.getLogger('logger')

handler1 = logging.StreamHandler()
handler2 = logging.FileHandler(filename='log.log',encoding="utf-8",mode='w')

logger.setLevel(logging.DEBUG)
handler1.setLevel(logging.WARNING)
handler2.setLevel(logging.DEBUG)


formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s ")
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)


logger.addHandler(handler1)
logger.addHandler(handler2)

# logger.debug('This is debug message,这是debug信息')
# logger.info('This is info message，这是info信息')
# logger.warning('This is warning message,这是warning信息')
# logger.error('This is error message')
# logger.critical('This is critical message')