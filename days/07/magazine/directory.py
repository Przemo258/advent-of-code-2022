from __future__ import annotations
from typing import Union
from .file import File


class Directory:
    name: str
    parent: Union[Directory, None]
    files: list[File]
    directories: list

    def __init__(self, name: str, parent: Union[Directory, None] = None,
                 files: list[File] = None, directories: list[Directory] = None):
        self.name = name
        self.parent = parent
        self.files = files if files is not None else []
        self.directories = directories if directories is not None else []

    def __str__(self):
        files_names = [file.name for file in self.files]
        dir_names = [directory.name for directory in self.directories]
        parent_name = self.parent.name if self.parent is not None else 'No parent'
        return f'Directory {self.name} with parent directory "{parent_name}"' \
               f' with files {files_names} and directories {dir_names} ' \
               f'and total size of {self.get_total_size()}'

    def add_file(self, file: File):
        if type(file) != File:
            raise TypeError(f'This is not a file this is {type(file)}')
        elif file not in self.files:
            file.set_parent(self)
            self.files.append(file)
        else:
            raise AttributeError('File already in files')

    def add_directory(self, directory: Directory):
        if type(directory) != Directory:
            raise TypeError(f'Type {directory} not supported')
        elif directory in self.directories:
            raise AttributeError('Directory already in directories')
        self.directories.append(directory)

    def set_parent(self, directory: Directory):
        self.parent = directory

    def get_parent(self) -> Directory:
        if self.parent is None:
            raise ValueError('Parent is none')
        return self.parent

    def get_directory(self, directory_name: str):
        matching = list(filter(lambda item: item.name == directory_name, self.directories))
        if len(matching) == 0:
            raise ValueError('No matching directories found')
        return matching[0]

    def get_total_size(self, max_size: int = None):
        return self.get_file_sizes() + self.get_directories_sizes()

    def get_file_sizes(self) -> int:
        return sum(self.files)

    def get_directories_sizes(self, max_size: int = None) -> int:
        total = 0
        for directory in self.directories:
            total += directory.get_total_size(max_size)
        return total

    def get_all_directories(self):
        dirs = [self]
        for directory in self.directories:
            dirs += directory.get_all_directories()
        return dirs
