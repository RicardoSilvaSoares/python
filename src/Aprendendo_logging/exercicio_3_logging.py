"""
Exemplo 3.

Como personalizar a mensagem do log.
"""
import logging as logg

logg_format = "%(asctime)s: %(levelname)s :  %(filename)s : Linha de chamada do log: %(lineno)d : %(message)s"

logg.basicConfig(filename="ex3.log",
                    filemode = "w", level = logg.DEBUG, #modo .DEBUG mostra tudo
                    format = logg_format)

logger = logg.getLogger("root")

def add(x:int , y:int) -> int:
    """Função efetua a soma de dois inteiros e retorna um inteiro. """
    if isinstance(x,int) & isinstance(y,int):
        logger.info(f"x: {x} - y: {y}")   
        return x+y
    else:
        logger.warning(
            f"x: {x} type : {type(x)} - y: {y} type : {type(y)}"
            )    
add(7,7)
add(5.6,9)
# x = input("x")
# y= input("y")
# add(x,y)
# ****-- REVER --> UTILIZANDO O INPUT OS VALORES DE X E Y SE TORNAN STRING DIFERENCIAR ISSO 
# PARA OS FORMATOS REAIS INT OU FLOAT --****.

