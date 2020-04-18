import os

def __walk(path):
    folders = []
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for folder in d:
            folders.append(os.path.join(r, folder))
        for file in f:
            files.append(os.path.join(r, file))
    return (folders, files)

class Dirdict:
    def swim(self):
        print("The shark is swimming.")

    def be_awesome(self):
        print("The shark is being awesome.")

def dir2dict(path):
    shark = Dirdict()
    shark.swim()
    #print(__walk(path))

dir2dict("path")
