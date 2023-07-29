import os
import shutil

from file_organizer import PdfOrganizer

from main import organize_files


def test_organize_files():
    organize_files()


def test_pdf_organizer():
    # create a temporary directory for testing
    temp_dir = os.path.join(os.getcwd(), "temp")
    os.makedirs(temp_dir, exist_ok=True)

    # create some test files
    file1 = os.path.join(temp_dir, "file1.pdf")
    with open(file1, "w") as f:
        f.write("test file 1")

    file2 = os.path.join(temp_dir, "file2.pdf")
    with open(file2, "w") as f:
        f.write("test file 2")

    # create the PdfOrganizer object and run the organize method
    pdf_organizer = PdfOrganizer(temp_dir)

    # loop over the files in the temporary directory
    for file in os.listdir(temp_dir):
        pdf_organizer.organize(file)

    # check if the files were moved to the correct folders
    assert os.path.exists(os.path.join(temp_dir, "PDFs", "file1.pdf"))
    assert os.path.exists(os.path.join(temp_dir, "PDFs", "file2.pdf"))

    # remove the temporary directory
    shutil.rmtree(temp_dir)


test_pdf_organizer()
test_organize_files()
