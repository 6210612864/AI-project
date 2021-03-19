import os

from myDataLib import FileManager


def main():
    #Choose your Folder and sent it's file to class
    data = [file for file in os.listdir("Glaucoma")]
    f = FileManager("Glaucoma")
    #Upload your file from list:data to your drive
    while len(data) != 0:
        file = data.pop()
        f.upload_file(f"Glaucoma/{file}", file)
        print(f"Uploaded {file}")


main()
