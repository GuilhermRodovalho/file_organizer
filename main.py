"""
Este script organiza todos os arquivos da minha pasta de downloads
em pastas de acordo com a extensão do arquivo. 
Caso não exista uma pasta para o tipo do arquivo, uma nova pasta
é criada. O script funciona para a maioria dos arquivos, porém nem todas
as extensões serão consideradas. Arquivos de imagem ficarão juntos
"""
import os
from typing import Optional

from file_organizer import FileOrganizer, PdfOrganizer, ImageOrganizer, ZipOrganizer

FOLDER_PATH = "/home/guilherme/Downloads"


def get_file_organizer(file_extension: str) -> Optional[FileOrganizer]:
    if file_extension[0] == ".":
        file_extension = file_extension[1:]

    if file_extension in PdfOrganizer.extensions_supported():
        return PdfOrganizer(FOLDER_PATH)
    elif file_extension in ImageOrganizer.extensions_supported():
        return ImageOrganizer(FOLDER_PATH)
    elif file_extension in ZipOrganizer.extensions_supported():
        return ZipOrganizer(FOLDER_PATH)

    return None


def get_file_extension(file_name: str):
    """
    Retorna a extensão do arquivo
    """
    return file_name.split(".")[-1]


def organize_files():
    for file in os.listdir(FOLDER_PATH):
        organizer = get_file_organizer(get_file_extension(file))
        if organizer:
            organizer.organize(file)


def main():
    organize_files()
