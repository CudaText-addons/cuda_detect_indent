Plugin for CudaText
It handles on_open event, and detects indentation for opened file:
tabs/spaces, number of spaces.

Code is based on Sublime Text's plugin detect_indentation.py.
It was open sourced at https://github.com/randy3k/sublime-default

Config file is supported: (CudaText)/settings/plugins.ini:

[detect_indent]
max_read_lines=40
min_indented_lines=10
hide_undetected_msg=0

Keys in ini-file are:
- max_read_lines: How much lines to read from file beginning.
- min_indented_lines: How much indented lines must occur for detection.
- hide_undetected_msg (bool, 0 or 1): Supress Console messages
                      "Detect Indent for 'nnn.txt': undetected"


Author: Alexey Torgashin (CudaText)
Lincese: MIT
