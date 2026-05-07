# ================================
# REDAX CLI - Validator
# ================================

import os
import re
from config.settings import SUPPORTED_EXTENSIONS, MAX_FILE_SIZE

# ─── Helper: Parse MAX_FILE_SIZE from settings ──────
def _parse_max_file_size() -> int:
    """Convert MAX_FILE_SIZE strign (e.g. '10MB') to bytes."""
    size_str = MAX_FILE_SIZE.upper().strip()
    if size_str.endswith("GB"):
        return int(size_str[:-2]) * 1024 * 1024 * 1024
    elif size_str.endswith("MB"):
        return int(size_str[:-2]) * 1024 * 1024
    elif size_str.endswith("KB"):
        return int(size_str[:-2]) * 1024
    else:
        return int(size_str)  # assume it's already in bytes
    
# ─── 1. Validate Path Exists ────────────────────────
def validate_path_exist(path: str) -> tuple[bool, str]:
    """
    Check if the given path exists on the filesystem.

    Returns:
       (True, "") if valid
       (False, error_message) if invalid

    Used by: move, remove, read, read_line commands
    """
    if not os.path.exists(path):
        return False, f"Error: Path '{path}' does not exist."
    return True, ""

# ─── 2. Validate Is File ────────────────────────────
def validate_is_file(path: str) -> tuple[bool, str]:
    """
    Check if the given path is a file (not a directory).

    Returns:
       (True, "") if valid
       (False, error_message) if invalid

    Used by: move, remove, read, read_line commands
    """
    valid, msg = validate_path_exist(path)
    if not valid:
        return False, msg
    
    if not os.path.isfile(path):
        return False, f"Error: Path '{path}' is not a file."
    return True, ""

# ─── 3. Validate Is Directory ───────────────────────
def validate_is_directory(path: str) -> tuple[bool, str]:
    """
    Check if the given path is a directory.

    Returns:
       (True, "") if valid
       (False, error_message) if invalid

    Used by: search, organize, create commands
    """
    valid, msg = validate_path_exist(path)
    if not valid:
        return False, msg
    
    if not os.path.isdir(path):
        return False, f"Error: Path '{path}' is not a directory."
    return True, ""

# ─── 4. Validate Has Permission ─────────────────────
def validate_has_permission(path: str, mode: str = "read") -> tuple[bool, str]:
    """
    Check if the app has permission to read or write the path.
 
    Args:
        path: File or folder path
        mode: "read" or "write"
 
    Returns:
        (True, "") if valid
        (False, error_message) if invalid
 
    Used by: organize, remove, move, create commands
    """
    valid, msg = validate_path_exist(path)
    if not valid:
        return False, msg
 
    if mode == "read" and not os.access(path, os.R_OK):
        return False, f"Error: No read permission for '{path}'."
    elif mode == "write" and not os.access(path, os.W_OK):
        return False, f"Error: No write permission for '{path}'."
    return True, ""

# ─── 5. Validate File Extension ─────────────────────
def validate_extension(path: str) -> tuple[bool, str]:
    """
    Check if the file's extension is in the SUPPORTED_EXRENSIONS list.

    Returns:
       (True, "") if valid
       (False, error_message) if invalid

    Used by: read, read_line, create commands
    """
    _, ext = os.path.splitext(path)
    if ext.lower() not in SUPPORTED_EXRENSIONS:
        return False, (
            f"❌ Unsupported file extension: '{ext}'\n"
            f"   Supported: {', '.join(SUPPORTED_EXTENSIONS)}"
        )
    return True, ""