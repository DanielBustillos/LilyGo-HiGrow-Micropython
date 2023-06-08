def open_text_file(path, json=True):
    """
    Opens a text file and returns its content.

    Parameters:
    - path (str): The path to the text file.
    - json (bool): Indicates whether the file contains JSON data.
                   Default is True.

    Returns:
    - data (str or list or dict): The content of the text file.
                                  If json is True, returns a dictionary or list parsed from JSON.
                                  Otherwise, returns a list of lines from the file.

    """
    import ujson
    
    with open(path) as fp:
        if json:
            data = ujson.load(fp)
        else:
            data = fp.readlines()

    return data
