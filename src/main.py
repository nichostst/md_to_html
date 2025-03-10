import os
import sys
import shutil

from copystatic import copy_files_recursive
from generatepage import generate_pages_recursive


basepath = ''
if sys.argv[1]:
    basepath = sys.argv[1]

dir_path_static = f"{basepath}/static"
dir_path_docs = f"{basepath}/docs"

def main():
    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)
    generate_pages_recursive(f'{basepath}/content/', 'template.html', 'docs/', basepath=basepath)


main()
