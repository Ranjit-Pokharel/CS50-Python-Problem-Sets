def main():
    # get name of file
    file_name = input("File name: ").lower().strip()

    # print type of file
    print(extensions(file_name))


def extensions(file_name):
    if "." in file_name:
        extension = file_name.split(".")[-1]
    else:
        extension = file_name
        
    extension_types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }

    if extension in extension_types:
        return extension_types[extension]
    return "application/octet-stream"

if __name__ == "__main__":
    main()