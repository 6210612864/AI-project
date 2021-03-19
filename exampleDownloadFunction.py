from myDataLib import FileManager


def main():
    # Select folder in your drive
    func = FileManager("Normal")
    # get list of dictionary in your folder
    data = func.clist_lfif()
    # download file by sent your list and index
    func.download_file(data[0])
    print("finish")
    # this will download n0001.png


main()
