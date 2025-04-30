# NoSQL with MongoDB

## 📚 Description

This project aims to teach the basics of NoSQL databases, particularly MongoDB, by exploring the difference between SQL and NoSQL, CRUD operations, and working with collections using the Mongo shell and PyMongo (Python). All scripts were tested on Ubuntu 20.04 with MongoDB 4.4 and Python 3.9.

---

## 🎯 Learning Objectives

By the end of this project, you will be able to:

- Understand what a NoSQL database is
- Differentiate between SQL and NoSQL
- Define the ACID acronym
- Explain the concept of document storage
- List the types of NoSQL databases
- Enumerate the advantages of a NoSQL database
- Query, insert, update, and delete data in MongoDB
- Use MongoDB both in the command line and in Python with PyMongo

---

## ✅ Technical Requirements

### MongoDB Shell Scripts

- Executed on Ubuntu 20.04 LTS with MongoDB 4.4
- All files must end with an empty line
- First line of files: `// my comment`
- Files tested with the `wc` command

### Python Scripts

- Python 3.9 with the `pymongo==4.8.0` library
- Compliance with `pycodestyle` standards (version 2.5.\*)
- Documentation required for modules and functions
- Executable files with `#!/usr/bin/env python3`
- No code execution upon import: `if __name__ == "__main__":`

---

## 🗃️ Task Overview

| #  | Title                          | File                        | Description |
|----|--------------------------------|-----------------------------|-------------|
| 0  | List all databases             | `0-list_databases`          | Lists all databases |
| 1  | Create a database              | `1-use_or_create_database`  | Creates or uses a `my_db` database |
| 2  | Insert document                | `2-insert`                  | Inserts a document into the `school` collection |
| 3  | All documents                  | `3-all`                     | Lists all documents |
| 4  | All matches                    | `4-match`                   | Finds documents where `name="Holberton school"` |
| 5  | Count                          | `5-count`                   | Counts the number of documents in the `school` collection |
| 6  | Update                         | `6-update`                  | Adds `address="972 Mission street"` |
| 7  | Delete by match                | `7-delete`                  | Deletes all documents where `name="Holberton school"` |
| 8  | List documents (Python)        | `8-all.py`                  | Python function to list all documents |
| 9  | Insert document (Python)       | `9-insert_school.py`        | Python function to insert a document using `**kwargs` |
| 10 | Update topics (Python)         | `10-update_topics.py`       | Updates the list of `topics` for a school |
| 11 | Schools by topic (Python)      | `11-schools_by_topic.py`    | Lists schools teaching a specific `topic` |
| 12 | Nginx log stats (Python)       | `12-log_stats.py`           | Displays statistics for Nginx logs in MongoDB |

---

## 🛠️ Installation

### MongoDB 4.4

Follow the official guide: [MongoDB Installation Guide](https://www.mongodb.com/docs/manual/installation/)

### PyMongo

```bash
pip install pymongo==4.8.0

## ✅ Tasks Overview

### 0. List Databases

Script that lists all databases present in MongoDB.  
> `0-list_databases`

---

### 1. Create or Use Database

Script to connect to (and create if necessary) a database called `my_db`.  
> `1-use_or_create_database`

---

### 2. Insert Document

Inserts one document into the `school` collection:
```json
{ "name": "Holberton school" }

## 🧪 Example Usage

$ python3 8-all.py
[]
$ python3 9-insert_school.py
ObjectId('...')

## 🔗 Author

Project by Holberton School.
MongoDB logic implemented using pymongo by Noumso.