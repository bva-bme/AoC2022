class File:
    def __init__(self, filepath, filename, filesize):
        self.filepath = filepath
        self.filename = filename
        self.filesize = filesize


class Folder:
    def __init__(self, folderpath, foldername):
        self.folderpath = folderpath
        self.foldername = foldername
        self.foldersize = 0
        self.subfolders = []
        self.files = []

    def add_subfolder(self, folderpath, foldername):
        tmp_folder = Folder(folderpath, foldername)
        self.subfolders.append(tmp_folder)

    def add_file(self, filepath, filename, filesize):
        tmp_file = File(filepath, filename, filesize)
        self.files.append(tmp_file)

    def find_subfolder_from_path(self, path):
        for p in path:
            if p == 'root':
                folder = self
            else:
                folder = self.find_subfolder(p, folder.subfolders)
        return folder

    @staticmethod
    def find_subfolder(dirname, subfolders):
        for folder in subfolders:
            if folder.foldername == dirname:
                return folder

    def update_foldersize(self, path, filesize):
        for p in path:
            if p == 'root':
                folder = self
            else:
                folder = self.find_subfolder(p, folder.subfolders)
            folder.foldersize += filesize


def scan_filestructure(lines):
    current_path = ['root']
    filestruct = Folder([], 'root')

    for line in lines:
        if line == '$ cd /\n':
            current_path = ['root']
        elif line == '$ cd ..\n':
            current_path.pop()
        elif line[0:5] == '$ cd ':
            current_path.append(line[5:])
        elif line == '$ ls\n':
            pass
        elif line[0:3] == 'dir':
            folder = filestruct.find_subfolder_from_path(current_path)
            st_exists = False
            for subfolder in folder.subfolders:
                if subfolder.foldername == line[4:]:
                    st_exists = True
            if not st_exists:
                folder.add_subfolder(current_path, line[4:])
        else:
            filedata = line.split()
            folder = filestruct.find_subfolder_from_path(current_path)
            st_exists = False
            for file in folder.files:
                if file.filename == filedata[1]:
                    st_exists = True
            if not st_exists:
                folder.add_file(current_path, filedata[1], int(filedata[0]))
            filestruct.update_foldersize(current_path, int(filedata[0]))

    return filestruct

def sum_below_thd(filestruct, thd): #breadth first search
    foldersize_thd_sum = 0

    visited = []  # List for visited nodes.
    queue = []  # Initialize a queue

    visited.append(filestruct)
    queue.append(filestruct)

    while queue:
        folder = queue.pop(0)
        if folder.foldersize < thd:
            foldersize_thd_sum += folder.foldersize
        for subfolder in folder.subfolders:
            if subfolder not in visited:
                visited.append(subfolder)
                queue.append(subfolder)

    return foldersize_thd_sum

def folder_to_delete(total_space, minimum_space, filestruct):
    space_needed = filestruct.foldersize + minimum_space - total_space

    space_to_get = total_space

    visited = []  # List for visited nodes.
    queue = []  # Initialize a queue

    visited.append(filestruct)
    queue.append(filestruct)

    while queue:
        folder = queue.pop(0)
        if folder.foldersize > space_needed and folder.foldersize < space_to_get:
            space_to_get = folder.foldersize
        for subfolder in folder.subfolders:
            if subfolder not in visited:
                visited.append(subfolder)
                queue.append(subfolder)

    return space_to_get

# Part I
file = open("input_day7.txt", 'r')
lines = file.readlines()

filestruct = scan_filestructure(lines)
thd = 100000
foldersize_thd_sum = sum_below_thd(filestruct, thd)
print(foldersize_thd_sum)

file.close()

# Part II
space_to_get = folder_to_delete(70000000, 30000000, filestruct)
print(space_to_get)