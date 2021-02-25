from .googledrive import download_file_from_google_drive


def merge_dict(a, b):
    b = b.copy()
    for k, v in a.items():
        if isinstance(v, dict) and k in b:
            if not isinstance(b[k], dict):
                raise TypeError
            b[k] = merge_dict(v, b[k])
        else:
            b[k] = v
    return b
