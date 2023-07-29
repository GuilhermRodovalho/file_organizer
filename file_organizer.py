from abc import ABC, abstractmethod
import os
from typing import List


# Exception for when creating a folder
class FolderCreationError(Exception):
    pass


class FileCreationError(Exception):
    pass


class FileTypeError(Exception):
    pass


class FileOrganizer(ABC):
    """Abstract class for file organizer"""

    this_folder = None

    def __init__(
        self,
        root_folder: str,
    ) -> None:
        self.root_folder = root_folder
        super().__init__()

    def organize(self, file_name: str):
        """
        Organize the file in the specific folder
        """
        self.check_file(file_name)
        self.create_folder()

        # Move the file to the PDFs folder
        try:
            os.rename(
                os.path.join(self.root_folder, file_name),
                os.path.join(self.this_folder, os.path.basename(file_name)),
            )
        except OSError as err:
            error_message = (
                f"Failed to move file {file_name} to {self.this_folder}: {err}"
            )
            print(error_message)
            raise FileCreationError(error_message)

    def create_folder(self):
        """
        Create a folder for the file type
        """
        if self.check_if_folder_exists():
            return
        try:
            os.mkdir(self.this_folder)
        except OSError as err:
            raise FolderCreationError(
                f"Creation of the directory {self.this_folder} failed: {err}"
            )

    def check_if_folder_exists(self) -> bool:
        if os.path.exists(self.this_folder) and os.path.isdir(self.this_folder):
            return True
        return False

    def check_file(self, file_name: str):
        file_extension = file_name.split(".")[-1]
        if file_extension not in self.extensions_supported():
            raise FileTypeError(f"File {file_name} is not a supported file type")

    @staticmethod
    def extensions_supported() -> List[str]:
        pass


class PdfOrganizer(FileOrganizer):
    def __init__(self, root_folder: str) -> None:
        super().__init__(root_folder=root_folder)
        self.this_folder = os.path.join(root_folder, "PDFs")

    @staticmethod
    def extensions_supported() -> List[str]:
        return ["pdf"]


class ImageOrganizer(FileOrganizer):
    def __init__(self, root_folder: str) -> None:
        super().__init__(
            root_folder=root_folder,
        )
        self.this_folder = os.path.join(root_folder, "Images")

    @staticmethod
    def extensions_supported() -> List[str]:
        return ["jpg", "png", "gif", "jpeg", "bmp", "svg", "webp", "ico"]


class ZipOrganizer(FileOrganizer):
    def __init__(self, root_folder: str) -> None:
        super().__init__(
            root_folder=root_folder,
        )
        self.this_folder = os.path.join(root_folder, "Zips")

    @staticmethod
    def extensions_supported() -> List[str]:
        return [
            "zip",
            "rar",
            "7z",
            "tar",
            "gz",
            "bz2",
            "xz",
            "z",
            "lzma",
            "tlz",
            "txz",
            "tbz2",
            "tbz",
            "tlzma",
            "txz",
            "tlz",
            "txz",
            "lz",
            "lzma",
            "lzo",
            "lzip",
            "lzop",
            "arj",
            "cab",
            "chm",
            "deb",
            "dmg",
            "egg",
            "iso",
            "jar",
            "msi",
            "msix",
            "msixbundle",
            "pak",
            "pkg",
            "rpm",
            "s7z",
            "shar",
            "tar",
            "tbz2",
            "tgz",
            "tlz",
            "war",
            "whl",
            "xpi",
            "zipx",
            "xz",
            "z",
            "zip",
        ]
