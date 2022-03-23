from functools import wraps
import logging as logg
from unittest import result

logg_format = "%(asctime)s: %(levelname)s :  %(filename)s : Linha de chamada do log: %(lineno)d : %(message)s"

logg.basicConfig(filename="Decorator",
                    filemode = "w", level = logg.DEBUG, #modo .DEBUG mostra tudo
                    format = logg_format)

logger = logg.getLogger("root")

def log(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        ls_sms=f'func{func}:args:{args}:kwargs{kwargs}:result:{result}'
        logger.debug(ls_sms)
        return result
    return inner
#decorar a função.
@log
def add(x,y):
    return x+y
add(7,7)