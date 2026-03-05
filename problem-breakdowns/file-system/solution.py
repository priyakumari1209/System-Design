# solution.py — File System

from datetime import datetime
from threading import Lock

class FileSystemItem:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_size(self):
        raise NotImplementedError

    def get_path(self):
        if self.parent is None:
            return "/" + self.name
        return self.parent.get_path() + "/" + self.name


class File(FileSystemItem):
    def __init__(self, name, content="", parent=None):
        super().__init__(name, parent)
        self.content = content

    def get_size(self):
        return len(self.content)

    def update_content(self, content):
        self.content = content
        self.updated_at = datetime.now()


class Folder(FileSystemItem):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.children = []
        self.lock = Lock()

    def add_child(self, item):
        with self.lock:
            item.parent = self
            self.children.append(item)

    def remove_child(self, item):
        with self.lock:
            self.children.remove(item)

    def get_size(self):
        return sum(child.get_size() for child in self.children)

    def list_contents(self):
        return [child.name for child in self.children]


class FileSystem:
    def __init__(self):
        self.root = Folder("root")

    def get_item(self, path):
        parts = path.strip("/").split("/")
        current = self.root
        for part in parts[1:]:  # skip "root"
            if isinstance(current, Folder):
                match = next(
                    (c for c in current.children if c.name == part), None
                )
                if not match:
                    return None
                current = match
            else:
                return None
        return current

    def create_file(self, folder_path, name, content=""):
        folder = self.get_item(folder_path)
        if not isinstance(folder, Folder):
            raise Exception("Path is not a folder")
        file = File(name, content, parent=folder)
        folder.add_child(file)
        return file

    def create_folder(self, parent_path, name):
        parent = self.get_item(parent_path)
        if not isinstance(parent, Folder):
            raise Exception("Path is not a folder")
        folder = Folder(name, parent=parent)
        parent.add_child(folder)
        return folder

    def delete(self, path):
        item = self.get_item(path)
        if not item or item.parent is None:
            return False
        item.parent.remove_child(item)
        return True

    def move(self, source_path, dest_path):
        item = self.get_item(source_path)
        dest = self.get_item(dest_path)
        if not item or not isinstance(dest, Folder):
            return False
        item.parent.remove_child(item)
        dest.add_child(item)
        return True

    def rename(self, path, new_name):
        item = self.get_item(path)
        if not item:
            return False
        item.name = new_name
        item.updated_at = datetime.now()
        return True

    def search(self, name, folder=None):
        if folder is None:
            folder = self.root
        results = []
        for child in folder.children:
            if child.name == name:
                results.append(child)
            if isinstance(child, Folder):
                results.extend(self.search(name, child))
        return results


# --- Run it ---
if __name__ == "__main__":
    fs = FileSystem()

    # create folders
    docs = fs.create_folder("/root", "documents")
    pics = fs.create_folder("/root", "pictures")

    # create files
    resume = fs.create_file("/root/documents", "resume.pdf", "Resume content here")
    photo  = fs.create_file("/root/pictures",  "photo.png",  "binary data here")

    # sizes
    print(f"resume size: {resume.get_size()}")
    print(f"documents folder size: {docs.get_size()}")
    print(f"total root size: {fs.root.get_size()}")

    # list
    print(f"root contents: {fs.root.list_contents()}")

    # search
    results = fs.search("resume.pdf")
    print(f"search result: {[r.get_path() for r in results]}")

    # move
    fs.move("/root/documents/resume.pdf", "/root/pictures")
    print(f"pictures after move: {pics.list_contents()}")

    # delete
    fs.delete("/root/pictures/photo.png")
    print(f"pictures after delete: {pics.list_contents()}")