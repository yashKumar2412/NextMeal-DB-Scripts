import tarfile

tar_path = "photos"

with tarfile.open(tar_path, "r") as tar:
    tar.extractall(path="photos_extracted")
    print("Files extracted successfully!")