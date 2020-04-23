#!/usr/bin/env python
from datetime import datetime

msg = [
    "This is a",
    "multiline message",
    "with a bunch of lines.",
    ]

print('::set-output name=msg::' + '%0A'.join(msg))

