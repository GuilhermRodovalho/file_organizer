"""
Este script organiza todos os arquivos da minha pasta de downloads
em pastas de acordo com a extensão do arquivo. 
Caso não exista uma pasta para o tipo do arquivo, uma nova pasta
é criada. O script funciona para a maioria dos arquivos, porém nem todas
as extensões serão consideradas. Arquivos de imagem ficarão juntos
"""
import os

FOLDER_PATH = "/home/guilherme/Downloads"


def get_file_extension(file_name: str):
    """
    Retorna a extensão do arquivo
    """
    return file_name.split(".")[-1]


def organize_files():
    for file in os.listdir(FOLDER_PATH):
        print(file)


def main():
    organize_files()
