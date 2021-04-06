# TerminalTitles


Make a comment title for source code. 

Adds two rows of equals signs and a title centred in uppercase.

The width is 80 characters.

Example (XML):
```xml
<!-- ======================================================================= -->
<!--                              HELLO, WORLD!                              -->
<!-- ======================================================================= -->
```

Tested and developed for Linux and Windows but should work properly on MacOs.

## Installation

**Python**

Python version 3.6 or above

_On Linux/Mac:_
```bash
python3 --version
```

_On Windows_:
```bash
python --version
```

**Clone the repository**

Git is required

```bash
git --version
```

Clone
```bash
git clone https://aymericdeschard@bitbucket.org/aymericdeschard/terminaltitles.git <where you want to install it>
```

**Dependencies**

Install dependencies:

_On Linux/Mac:_
```bash
pip3 install -r requirements.txt
```

_On Windows_:
```bash
pip install -r requirements.txt
```

**Make it executable**

Linux and MacOs only
```bash
chmod +x TerminalTitles.py
```

**Bash shortcut**

If you want to access it directly from the terminal (Linux and MacOsX) with the command `titles`:
```bash
INSTALL_DIR="<the full path to the installation directory>"
printf "# TerminalTitles\nalias titles='${INSTALL_DIR}/TerminalTitles.py'" >> ~/.bash_aliases
```

**Update**

```bash
git pull
```

## Managing languages
The languages available can be changed by editing `languages.json` in the root directory of the script.
```json
{
    "0": {
        "name": "XML",
        "beginComment": "<!--",
        "endComment": "-->"
    },
    "1": {
        "name": "Python/Bash",
        "beginComment": "#"
    },
    "2": {
        "name": "C-like",
        "beginComment": "/*",
        "endComment": "*/"
    }
}
```

The **order** of appearance can be modified by changing its corresponding key, though the keys should be continuous starting from 0 (the order in the json doesn't matter). The "other" option will always be at the end.

The **name** they appear can be changed by the value of `name`, etc. for the start of the line comment (`beginComment`) and the optional end of the line comment (`endComment`).

To **add** a new language, just add a dictionary (`endComment` is optional).

