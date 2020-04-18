import os

class Dirdict:
    def __init__(self, path):
        self.path = os.path.abspath(path)

    def __walk(self, path):
        folders = []
        files = []
        for r, d, f in os.walk(path):
            for folder in d:
                folders.append(os.path.abspath(os.path.join(r, folder)))
            for file in f:
                files.append(os.path.abspath(os.path.join(r, file)))
        return (sorted(folders), sorted(files))

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

data = Dirdict("sample")
data.allfilepaths()
data.alldirpaths()
data.allfilenames()
data.alldirnames()
