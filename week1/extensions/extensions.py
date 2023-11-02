import mimetypes

def get_media_type(filename):
    suffix = filename.lower().split(".")[-1]
    media_type = mimetypes.guess_type(filename, strict=False)[0]
    if media_type is None:
        media_type = mimetypes.types_map.get(f".{suffix}", 'application/octet-stream')
    return media_type

filename = input("Please Enter the file name: ")
media_type = get_media_type(filename)
print(f"{media_type}")