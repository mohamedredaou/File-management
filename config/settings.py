# ================================
# REDAX CLI - Configuration Settings
# ================================

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# ─── App Info ───────────────────────────────────────
APP_NAME = os.getenv("APP_NAME", "REDAX CLI")
VERSION  = os.getenv("VERSION", "1.0.0")

# ─── Default Paths ──────────────────────────────────
DEFAULT_PATH = os.getenv("DEFAULT_PATH", "./")
LOG_PATH     = os.getenv("LOG_PATH", "./logs")

# ─── File Settings ──────────────────────────────────
MAX_FILE_SIZE = os.getenv("MAX_FILE_SIZE", "10MB")

SUPPORTED_EXTENSIONS = os.getenv(
    "SUPPORTED_EXTENSIONS",
    ".txt,.pdf,.docx,.xlsx,.csv,.py,.json,.xml,.html,.jpg,.png"
).split(",")  # converts the string into a list

# ─── Organize Categories ────────────────────────────
# Used by commands/organize.py to sort files into folders
FILE_CATEGORIES = {
    "Images"    : [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents" : [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"],
    "Code"      : [".py", ".js", ".html", ".css", ".json", ".xml", ".ts"],
    "Archives"  : [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Videos"    : [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Audio"     : [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Others"    : []  # anything that doesn't match goes here
}