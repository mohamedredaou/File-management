# 📁 File REDAX CLI

A simple and powerful command-line tool to manage your files — search, move, remove, read, and organize files directly from your terminal.

---

## 🚀 Features

- 🔍 **Search** files by name or extension
- 📦 **Organize** files automatically by type or date
- 🚚 **Move** files from one location to another
- 🗑️ **Remove** files safely
- 📖 **Read** full file content in the terminal
- 🔢 **Read Line** — read a specific line number from a file
- 📝 **Create** new `.txt` files instantly

---

## 📂 Project Structure

```
REDAX-CLI/
│
├── main.py                  ← Entry point
├── requirements.txt         ← Dependencies
├── README.md                ← You are here
├── .env                     ← Environment variables (optional)
│
├── commands/                ← One file per CLI command
│   ├── __init__.py
│   ├── organize.py
│   ├── search.py
│   ├── move.py
│   ├── remove.py
│   ├── read.py
│   ├── read_line.py
│   └── create.py
│
├── core/                    ← Core logic & utilities
│   ├── __init__.py
│   ├── file_handler.py
│   ├── validator.py
│   └── formatter.py
│
├── config/                  ← App configuration
│   ├── __init__.py
│   └── settings.py
│
└── tests/                   ← Unit tests
    ├── __init__.py
    ├── test_search.py
    ├── test_move.py
    ├── test_remove.py
    └── test_read.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/file-manager.git
cd file-manager
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Usage

Run the CLI using:

```bash
python main.py <command> [options]
```

---

## 📋 Commands

### 🔍 Search
Search for files by name or extension in a directory.

```bash
python main.py search --name "report"
python main.py search --ext ".txt" --path "./documents"
```

| Option | Description |
|--------|-------------|
| `--name` | File name to search for |
| `--ext` | File extension (e.g. `.txt`, `.pdf`) |
| `--path` | Directory to search in (default: current dir) |

---

### 📦 Organize
Automatically organize files in a folder by type or date.

```bash
python main.py organize --path "./downloads"
```

| Option | Description |
|--------|-------------|
| `--path` | Directory to organize |

---

### 🚚 Move
Move a file to a new location.

```bash
python main.py move --src "./old/file.txt" --dest "./new/"
```

| Option | Description |
|--------|-------------|
| `--src` | Source file path |
| `--dest` | Destination directory or path |

---

### 🗑️ Remove
Delete a file permanently.

```bash
python main.py remove --path "./file.txt"
```

| Option | Description |
|--------|-------------|
| `--path` | Path to the file to delete |

> ⚠️ **Warning:** This action is irreversible. Make sure you want to delete the file.

---

### 📖 Read
Read and display the full content of a file.

```bash
python main.py read --path "./notes.txt"
```

| Option | Description |
|--------|-------------|
| `--path` | Path to the file to read |

---

### 🔢 Read Line
Read a specific line number from a file.

```bash
python main.py read-line --path "./notes.txt" --line 5
```

| Option | Description |
|--------|-------------|
| `--path` | Path to the file |
| `--line` | Line number to read (starts at 1) |

---

### 📝 Create
Create a new `.txt` file.

```bash
python main.py create --name "todo" --path "./"
```

| Option | Description |
|--------|-------------|
| `--name` | Name of the new file (without extension) |
| `--path` | Directory where the file will be created |

---

## 🧪 Running Tests

```bash
python -m pytest tests/
```

---

## 📦 Dependencies

```
rich       # Beautiful terminal output
click      # CLI argument handling (optional)
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)

---

> Built with 🐍 Python
