"""
psets1/extensions
-----------------
    a program that prompts the user for the name of a file
    and then outputs that file's media type if the file's name ends,
    case-insensitively, in any of these suffixes:

Supports
--------
    .gif
    .jpg
    .jpeg
    .png
    .pdf
    .txt
    .zip
"""


def main() -> None:
    """
    ask user for the name of the file
    evaluate it and gives type

    Parameters
    ----------
    - None
    Returns
    -------
    - None
    """
    # get name of file
    file_name: str = input("File name: ").lower().strip()

    # print type of file
    print(extensions(file_name))


def extensions(
    file_name: str,
    extension_types: dict = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    },
) -> str:
    """
    evaluate the file extensions

    Parameters
    ----------
    - file_name : str
        The name of the file to evaluate, including its extension.

    - extension_types : dict, optional
        A dictionary mapping file extensions to types. Defaults to a predefined dictionary
        including common extensions like "gif", "jpg", "jpeg", "png", "pdf", "txt", and "zip".

    Returns
    -------
    - str: type of file
    """
    if "." in file_name:
        extension = file_name.split(".")[-1]
    else:
        extension = file_name

    if extension in extension_types:
        return extension_types[extension]
    return "application/octet-stream"


if __name__ == "__main__":
    main()
