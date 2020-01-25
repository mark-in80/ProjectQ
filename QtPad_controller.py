def ReadFile(open_fname):
    """
    just test this function as usual.
    :param open_fname:
    :return:
    """
    openedFile = open(open_fname, 'r')
    txt_1 = openedFile.read()
    openedFile.close()
    return txt_1


def SaveFile(save_fname, blob):
    with open(save_fname, "w", encoding="utf-8") as function_save:
        function_save.write(blob)
