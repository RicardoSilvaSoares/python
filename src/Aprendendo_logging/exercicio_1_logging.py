"""
Exemplo 1.

explicação de nivel/level do log
"""
import logging as log

# Notamos que se escrevermos log.debug("mensagem"), ou log.info("menaagem")
# nao ira printar essas mensagem pelo nivel de criticidade 
# diferentemente do .warning, .erros , .critical

log.warning("Olá, estamos debugando o sistema...")
log.critical("critical")
log.error("error")