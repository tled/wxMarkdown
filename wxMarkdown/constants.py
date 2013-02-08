#!/bin/env/python

import os

#constants

HEAD= u"""
<html>
<head>
<title>%s</title>
<style type="text/css">
%s
</style>
</head>
<body>
"""

FOOT = u"""
</body>
</html>"""

CSS = "body { margin: 0.5em; color: %s; background-color: %s }"

try:
    cssf = open(os.path.join(os.path.expanduser('~'),'.config/wxmdv/style.css'))
    CUSTOM_CSS = cssf.read()
    cssf.close()
except:
    CUSTOM_CSS = """
pre,code{ 
    font-family: monospace;
}

h1,h2,h3,h4,h5,h6 {
	font-family: sans-serif;
}

p {
    text-align: justify;
    font-family: serif;
}

"""
