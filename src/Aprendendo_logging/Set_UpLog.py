import logging as logg
import logging.config

logging.config.fileConfig("simple_loggin.ini")
# get logger (root,banana), sendo que o root sempre é chamado
logger = logg.getLogger('banana')


logger.info("Set Log")
