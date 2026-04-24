import requests
import gzip
import shutil


def import_gz_file(url, path):

    response = requests.get(url, stream=True)

    with open(path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print('File downloaded')


def unpack_gz(path, new_path):

    with gzip.open(path, 'rb') as f_src:
        with open(new_path, 'wb') as f_dst:
            shutil.copyfileobj(f_src, f_dst)

    print("Gzip unpacked")