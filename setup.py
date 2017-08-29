#!/usr/bin/env python3

import os
import re

from distutils.core import setup

init_path = os.path.join(os.path.dirname(__file__),
                         "radicale_infcloud", "__init__.py")
with open(init_path) as f:
    version = re.search(r'VERSION = "([^"]+)"', f.read()).group(1)

setup(
    name="radicale_imap_auth",
    version=version,
    description="IMAP Auth for Radicale",
    url="https://github.com/ayevee/radicale_imap_auth",
    packages=["radicale_imap_auth"])
