import pathlib
from threading import Thread

extensions = {'text': ['.txt'], 'dll': ['.dll'], 'log': ['.log']}


def create_folder_from_list(folder_names):
    for folder in folder_names:
        if not pathlib.Path.is_dir(pathlib.Path.cwd() / 'files' / f'{folder}'):
            pathlib.Path.mkdir(pathlib.Path.cwd() / 'files' / f'{folder}')


def move_file(file_path):
    ext_list = list(extensions.items())
    for dict_key_int in range(len(ext_list)):
        if file_path.suffix in ext_list[dict_key_int][1]:
            print(f"Moving {file_path.name}  in  folder {pathlib.Path.cwd() / f'{ext_list[dict_key_int][0]}'}")
            file_path.rename(pathlib.Path.cwd() / 'files' / f'{ext_list[dict_key_int][0]}' / file_path.name)


if __name__ == '__main__':
    create_folder_from_list(extensions)

    for file_path in pathlib.Path('files').glob('**/*.*'):
        th = Thread(target=move_file, args=(file_path,),)
        th.start()
