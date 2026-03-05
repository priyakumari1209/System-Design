# Problem: File System

## Requirements

### Functional
- Create a file or folder
- Delete a file or folder
- Move a file or folder
- Rename a file or folder
- Search for a file or folder by name
- Get size of a file or folder
  - File size = its own content size
  - Folder size = sum of all children sizes
- List contents of a folder

### Non-Functional
- In-memory (no actual disk)
- Support deeply nested folders
- Concurrency: multiple users reading/writing at same time

---

## Core Entities

### FileSystemItem (Abstract Base)
- id
- name
- createdAt
- updatedAt
- parent (reference to parent folder)

### File (extends FileSystemItem)
- content (string or bytes)
- size (length of content)

### Folder (extends FileSystemItem)
- children (list of FileSystemItems)
- size = sum of all children sizes (recursive)

### FileSystem
- root (top level Folder)
- handles all operations

---

## APIs / Methods

| Class       | Method                                 | Returns          |
|-------------|----------------------------------------|------------------|
| FileSystem  | createFile(path, name, content)        | File             |
| FileSystem  | createFolder(path, name)               | Folder           |
| FileSystem  | delete(path)                           | bool             |
| FileSystem  | move(sourcePath, destinationPath)      | bool             |
| FileSystem  | rename(path, newName)                  | bool             |
| FileSystem  | search(name)                           | list of items    |
| FileSystem  | getItem(path)                          | FileSystemItem   |
| Folder      | addChild(item)                         | void             |
| Folder      | removeChild(item)                      | void             |
| Folder      | getSize()                              | int              |
| Folder      | listContents()                         | list             |
| File        | getSize()                              | int              |
| File        | updateContent(content)                 | void             |

---

## Design Decisions

- **Why Abstract base class FileSystemItem?**
  - File and Folder share common fields: name, id, parent
  - Avoids repeating same fields in both classes
  - Polymorphism: treat File and Folder the same way in search/move

- **Why getSize() on both File and Folder?**
  - Composite Pattern
  - Caller doesn't need to know if it's a file or folder
  - Just calls getSize() on anything
  - Folder getSize() recursively adds up all children

- **Why FileSystem is the orchestrator?**
  - Handles path resolution (find the right folder/file)
  - Folder and File don't know about paths
  - Keeps File and Folder classes focused on their own data

- **Why parent reference in FileSystemItem?**
  - Easy to move items (just update parent reference)
  - Easy to build full path by walking up parent chain

- **Concurrency concern**
  - Two users creating files in same folder at same time
  - Fix: lock the folder's children list during add/remove

---

## Composite Pattern (Key concept here)
```
FileSystemItem (abstract)
    ├── File          → getSize() = content length
    └── Folder        → getSize() = sum of all children getSize()
                        children can be Files OR more Folders
```

This means:
- Folder containing 3 files → size = file1 + file2 + file3
- Folder containing folder + file → size = innerFolder.getSize() + file.getSize()
- Works infinitely deep — no special cases needed

---

## Path Resolution Logic
```
Path: /root/documents/resume.pdf

Steps:
1. Start at root folder
2. Split path → ["root", "documents", "resume.pdf"]
3. Walk down:
   root → find "documents" in children
   documents → find "resume.pdf" in children
4. Return resume.pdf
```

---

## Search Logic
```
search(name):
  start at root
  for each item in folder:
    if item.name == name → add to results
    if item is Folder → recurse into it
  return all results
```

---

## Code
- See solution.py

---

## What I Learned
- Composite Pattern: treat File and Folder uniformly
- Recursive getSize() — folders delegate to children
- FileSystem owns path logic, not File/Folder
- Parent reference makes move operation simple
- Abstract base class removes duplication between File and Folder