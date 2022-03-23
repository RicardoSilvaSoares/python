#usando logging no try -except
import logging as logg

logg.basicConfig(filename = "try_except.log",
                    filemode = 'w', level = logg.DEBUG)

try:
    1/0
except Exception as e:
    logg.warning(f'{e} ' + "--> Nao e possivel dividir por 0 ")
    #se usarmos na linha seguinte "pass" nao ira alterar em nada