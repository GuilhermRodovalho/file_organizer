"""
Este script organiza todos os arquivos da minha pasta de downloads
em pastas de acordo com a extensão do arquivo. 
Caso não exista uma pasta para o tipo do arquivo, uma nova pasta
é criada. O script funciona para a maioria dos arquivos, porém nem todas
as extensões serão consideradas. Arquivos de imagem ficarão juntos
"""

import os
from typing import Optional

from file_organizer import (
    FileOrganizer,
    PdfOrganizer,
    ImageOrganizer,
    ZipOrganizer,
    EpubOrganizer,
)

STANDARD_FOLDER_PATH = "/home/guilherme/Downloads"


def get_file_organizer(
    file_extension: str, folder_path: str = STANDARD_FOLDER_PATH
) -> Optional[FileOrganizer]:
    if file_extension[0] == ".":
        file_extension = file_extension[1:]

    if file_extension in PdfOrganizer.extensions_supported():
        return PdfOrganizer(folder_path)
    elif file_extension in ImageOrganizer.extensions_supported():
        return ImageOrganizer(folder_path)
    elif file_extension in ZipOrganizer.extensions_supported():
        return ZipOrganizer(folder_path)
    elif file_extension in EpubOrganizer.extensions_supported():
        return EpubOrganizer(folder_path)

    return None


def get_file_extension(file_name: str):
    """
    Retorna a extensão do arquivo
    """
    return file_name.split(".")[-1]


def organize_files(folder_path: str = STANDARD_FOLDER_PATH):
    for file in os.listdir(folder_path):
        organizer = get_file_organizer(get_file_extension(file))
        if organizer:
            organizer.organize(file)


def organize_epub_files():
    home = os.path.expanduser("~")
    for dirpath, dirnames, filenames in os.walk(home):
        for file in filenames:
            if file.endswith(".epub"):
                organizer = get_file_organizer(get_file_extension(file), STANDARD_FOLDER_PATH)
                if organizer:
                    organizer.organize(os.path.join(dirpath, file))


def main(path: str = STANDARD_FOLDER_PATH):
    # organize_files(folder_path=path)
    organize_epub_files()
