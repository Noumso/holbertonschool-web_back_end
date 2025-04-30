# Pagination Project

This project demonstrates various techniques to implement pagination on a dataset, using Python. The dataset used is `Popular_Baby_Names.csv`, containing baby name data from NYC.

## 📚 Learning Objectives

By completing this project, you will be able to:

- Paginate a dataset using simple `page` and `page_size` parameters
- Enhance pagination with hypermedia metadata
- Implement deletion-resilient pagination

---

## 🛠️ Requirements

- Python 3.9
- Code must follow `pycodestyle` (version 2.5.\*)
- Each Python file must:
  - Start with `#!/usr/bin/env python3`
  - End with a new line
  - Include module and function-level docstrings
  - Use type annotations
- Dataset: [`Popular_Baby_Names.csv`](https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv)

---

## 📁 Project Structure

.
├── .gitignore
├── 0-main.py
├── 0-simple_helper_function.py
├── 1-main.py
├── 1-simple_pagination.py
├── 2-hypermedia_pagination.py
├── 2-main.py
├── 3-hypermedia_del_pagination.py
├── 3-main.py
├── Popular_Baby_Names.csv
├── README.md

---

## ✅ Tasks Overview

### 0. Simple Helper Function

Implement `index_range(page, page_size)` that returns a tuple of start and end indexes.

### 1. Simple Pagination

Class `Server` loads and caches the dataset.
Method `get_page(page, page_size)` returns the correct page of data using `index_range`.

Includes assertions:
- `page` and `page_size` must be positive integers.

### 2. Hypermedia Pagination

Adds method `get_hyper(page, page_size)` to the `Server` class.

Returns a dictionary with:
- `page_size`
- `page`
- `data`
- `next_page`
- `prev_page`
- `total_pages`

### 3. Deletion-Resilient Hypermedia Pagination

Implements method `get_hyper_index(index, page_size)` for robust pagination in case of dataset mutations (like row deletions).

Returns:
- `index`: start index of page
- `next_index`: index to use for next request
- `page_size`
- `data`

---

## 🧪 Example Usage

```bash
$ ./1-main.py
AssertionError raised with negative values
AssertionError raised with 0
AssertionError raised when page and/or page_size are not ints
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ...]

## 🔗 Author

Project by Holberton School.
Pagination logic by Noumso.