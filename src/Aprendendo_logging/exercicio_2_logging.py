"""
Exemplo 2.

Como escrever o log em um arquivo
"""

from imp import cache_from_source
import logging as log

log.basicConfig(filename = "ex2.log",
                filemode = 'w', level = log.DEBUG)
# -Podemos notar que quando o (filemode = "a" )-->default , os warnings sao gravados
# quantas vezes forem executados e sao salvos no arquivos ex2.log, mas caso 
# seja filemode= "w" será escrito apenas uma vez
log.debug("Ola, Estamos no arquivo")
log.info("Ola, Estamos no arquivo")
log.warning("Ola, Estamos no arquivo")
log.critical("Ola, Estamos no arquivo")
log.error("Ola, Estamos no arquivo")

#obs: quando usamos .debug chamamos a função e quando usamor.DEBUG estamos nos 
# referindo a um level

log.log(50,"Estamos on ")

#notamos que no metodo .log() ao definir o primeiro parametro onde foi definido a criticidade
#podemos obter notset(0),debug(10),info(20),warning(30),error(40),critical(50)