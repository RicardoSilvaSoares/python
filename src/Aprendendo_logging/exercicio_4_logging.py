"""
    Exemplo 4.

    Explicação de todas etapas do logger
"""
from asyncio.log import logger
import logging as logg

#criando obj logger 
logger = logg.getLogger()
#criando o level
logger.setLevel(logg.DEBUG)
#criando o formato
formatter = logg.Formatter("%(asctime)s: %(levelname)s :  %(filename)s : Linha de chamada do log: %(lineno)d : %(message)s")
# console handler
ch = logg.StreamHandler()
ch.setLevel(logg.DEBUG)
ch.setFormatter(formatter)
#handler que escreve no arquivo
fh = logg.FileHandler("ex4.log")
fh.setLevel(logg.DEBUG)
fh.setFormatter(formatter)

#adicionando handler ao objeto logging
logger.addHandler(fh)
logger.addHandler(ch)

logg.debug("OLÁ")

