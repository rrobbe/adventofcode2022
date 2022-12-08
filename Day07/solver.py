data = [line.replace("\n", "") for line in open('input', 'r')]


class File:
    def __init__(self, name, size):
        self.files = []
        self.directories = []
        self.name = name
        self.size = size

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size


class Directory:
    def __init__(self, name, parent=None):
        self.directories = []
        self.files = []
        self.name = name
        self.parent = parent

    def add_directory(self, d_name):
        if d_name not in [
            directory.get_name() for directory in self.directories
        ]:
            directory = Directory(d_name, self)
            self.directories.append(directory)
        else:
            print(f"Directory {d_name} already exists, skipping..")

    def add_file(self, f_name, f_size):
        if f_name not in [file.get_name() for file in self.files]:
            f = File(f_name, f_size)
            self.files.append(f)
        else:
            print(f"File {f_name} already exists in directory, skipping..")

    def get_directory(self, d_name):
        # filter: https://stackoverflow.com/a/290440
        return next(
            filter(lambda x: x.get_name() == d_name, self.directories), None
        )

    def get_directories(self, recursive=False):
        for parent_directory in self.directories:
            # yield: https://stackoverflow.com/a/231855
            yield parent_directory
            if recursive:
                directories = parent_directory.get_directories(recursive=True)
                for sub_directory in directories:
                    yield sub_directory

    def get_name(self):
        return self.name

    def get_size(self):
        size = 0
        for file in self.files:
            size += file.get_size()
        for directory in self.directories:
            size += directory.get_size()
        return size

    def change_to_parent_directory(self):
        return self.parent


class FileSystem:
    def __init__(self):
        self.root_dir = Directory("/")
        self.cwd = self.root_dir

    def get_cwd(self):
        return self.cwd

    def get_root_dir(self):
        return self.root_dir


class Terminal:
    def __init__(self):
        self.filesystem = FileSystem()

    def change_directory(self, dir_name):
        if dir_name == "/":
            self.filesystem.cwd = self.filesystem.root_dir
        elif dir_name == "..":
            self.filesystem.cwd = (
                self.filesystem.cwd.change_to_parent_directory()
            )
        else:
            self.filesystem.cwd = self.filesystem.cwd.get_directory(dir_name)

    def execute_commands(self, commands):
        for cmd in commands:
            if cmd.startswith("$"):
                output = cmd.split()
                binary = output[1]
                arg = ""
                if len(output) == 3:
                    arg = cmd.split()[2]
                if 'cd' in cmd:
                    self.change_directory(arg)
            else:
                if cmd.startswith("dir"):
                    dir_name = cmd.split()[1]
                    self.filesystem.cwd.add_directory(dir_name)
                else:
                    f_size, f_name = cmd.split()
                    self.filesystem.cwd.add_file(f_name, int(f_size))

    def find_sum_of_all_directories_with_max_size_100000(self):
        directories = self.filesystem.root_dir.get_directories(recursive=True)
        total_size = 0
        for directory in directories:
            directory_size = directory.get_size()
            if directory_size <= 100000:
                total_size += directory_size
        print(f"Total sum of directories with max size 100000 = {total_size}")

    def find_smallest_directory_to_delete_to_upgrade(self):
        sizes_of_candidates_to_delete = []
        directories = self.filesystem.root_dir.get_directories(recursive=True)

        total_used = self.filesystem.root_dir.get_size()
        size_to_free = total_used - 40000000

        for directory in directories:
            directory_size = directory.get_size()
            if directory_size > size_to_free:
                sizes_of_candidates_to_delete.append(directory_size)

        print(
            f"The size of the smallest directory to delete to "
            f"free enough space: {min(sizes_of_candidates_to_delete)}"
        )


terminal = Terminal()
terminal.execute_commands(data)
terminal.find_sum_of_all_directories_with_max_size_100000()
terminal.find_smallest_directory_to_delete_to_upgrade()
