Plugin for CudaText
It handles on_open event, and detects indentation for opened file:
tabs/spaces, number of spaces.

Code is based on Sublime Text's plugin detect_indentation.py.
It is open source at https://github.com/randy3k/sublime-default

Config file is supported: (CudaText)/settings/plugins.ini:

[detect_indent]
max_read_lines=40
min_indented_lines=10

Keys are:
- max_read_lines: How much lines to read from file beginning.
- min_indented_lines: How much indented lines must occur for detection.


Author: Alexey Torgashin (CudaText)
Lincese: MIT
