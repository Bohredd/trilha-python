import ctypes

atributoOcultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('./Ocultador de Arquivos/ocultar.txt', atributoOcultar)

if retorno:
    print("Arquivo ocultado")
else:
    print("Não ocultado...")
