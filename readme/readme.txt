Plugin for CudaText
It handles on_open event, and detects indentation for opened file:
tabs/spaces, number of spaces.

Code is based on Sublime Text's plugin detect_indentation.py.
It is open source at https://github.com/randy3k/sublime-default

Config file is supported: (CudaText)/settings/plugins.ini,
keys in section "detect_indent" are:
- "max_read_lines" (default 40): How much lines to read from file beginning.
- "min_indented_lines" (default 10): How much indented lines must occur for detection.


Author: Alexey Torgashin (CudaText)
Lincese: MIT
