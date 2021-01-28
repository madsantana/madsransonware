#!/usr/bin/python3.6

#Um ransonware simples codado em pyhton a título de estudos
#O material de base foi um curso gratuíto na Udemy
#
#Autor: Marco Antonio Damaceno
#Data: 21/01/2021
#
#Módulo de Descoberta de Arquivos


import os

def discovery(initial_path):
    extensions = [
            # 'exe', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img' "Arquivos do Sistema"
            'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', #imagens
            'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape', #audios
            'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', #videos
            'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', #office
            'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', #openoffice, adobe, e outros
            'yml', 'yaml', 'json', 'xml', 'csv', #estruturado e config
            'db', 'sql', 'dbf', 'mdb', 'iso', #bancos de dados
            'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', #linguagens web
            'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', #codigo fonte c e c++
            'java', 'class', 'jar', #codigo fonte  java
            'ps', 'bat', 'vb', #scritps microsft
            'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', #scripts unix linux
            'go', 'py', 'pyc', 'bf', 'coffee', #outros
            'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak', #compactados e backup
            ]
    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, _file))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path


#Este trecho não é executado se vc roda o módulo diretamente
if __name__ == '__main__':
    x = discovery(os.getcwd())
    for i in x:
        print(i)

