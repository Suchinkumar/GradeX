from zipfile import ZipFile


def extractAndList(filepath, probNumber, fileExtension):
    # print("--Inside extractAndList")
    # print("--"+fileExtension)
    all_files = []
    with ZipFile(filepath, 'r') as zipObj:
        file_names = zipObj.namelist()
        # print("--")
        # print(file_names)
        if probNumber:
            for file in file_names:
                if file.startswith(probNumber) and file.endswith(fileExtension):
                    zipObj.extract(file, filepath[:len(filepath) - 4])
                    all_files.append(file)
        else:
            for file in file_names:
                if file.endswith(fileExtension):
                    zipObj.extract(file, filepath[:len(filepath) - 4])
                    all_files.append(file)
    return all_files
