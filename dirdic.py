import os
from functools import reduce

class Dirdict:
    def __init__(self, path):
        self.path = os.path.abspath(path)

    def __directorystructure(self, rootdir):
        dir = {}
        rootdir = rootdir.rstrip(os.sep)
        start = rootdir.rfind(os.sep) + 1
        for path, dirs, files in os.walk(rootdir):
            folders = path[start:].split(os.sep)
            subdir = dict.fromkeys(files)
            parent = reduce(dict.get, folders[:-1], dir)
            parent[folders[-1]] = subdir
        return dir

    def __walk(self, path):
        folders = []
        files = []
        for r, d, f in os.walk(path):
            for folder in d:
                folders.append(os.path.abspath(os.path.join(r, folder)))
            for file in f:
                files.append(os.path.abspath(os.path.join(r, file)))
        return (sorted(folders), sorted(files))

    def __foldersize(self, folder):
        total_size = os.path.getsize(folder)
        for item in os.listdir(folder):
            itempath = os.path.join(folder, item)
            if os.path.isfile(itempath):
                total_size += os.path.getsize(itempath)
            elif os.path.isdir(itempath):
                total_size += self.__foldersize(itempath)
        return total_size

    def size(self):
        print(self.__foldersize(self.path))

    def allfilepaths(self):
        print(self.__walk(self.path)[1])

    def alldirpaths(self):
        print(self.__walk(self.path)[0])

    def allfilenames(self):
        filenames = []
        for p in self.__walk(self.path)[1]:
            filename=os.path.basename(p)
            filenames.append(filename)
        print(filenames)

    def alldirnames(self):
        dirnames = []
        for d in self.__walk(self.path)[0]:
            dirname=os.path.basename(d)
            dirnames.append(dirname)
        print(dirnames)

    def getcontent(self, path):
        if os.path.isfile(path):
            f = open(path, "r")
            print(f.read())
        else:
            print ("File not exist")

    def dir(self):
        print(self.__directorystructure(self.path))

data = Dirdict("sample")
data.allfilepaths()
data.alldirpaths()
data.allfilenames()
data.alldirnames()
data.size()
data.dir()
data.getcontent("/Users/mike/Desktop/dirdic/sample/b/2.txt")
