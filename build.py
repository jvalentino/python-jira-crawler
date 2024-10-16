#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, Author
import sys

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
# use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('python.install_dependencies')

name = "python-jira-crawler"
version = "1.0.0"
authors = [Author("John Valentino", "your.email@example.com")]
license = "MIT"
summary = "An example Python application built with PyBuilder"
url = "https://example.com"

default_task = "publish"

@init
def set_properties(project):
    project.build_depends_on("mockito")
    project.depends_on("requests")
    project.depends_on("Pillow")
    project.depends_on("PyYAML")
    
    # Check for tkinter
    try:
        import tkinter
    except ImportError:
        sys.exit("Error: tkinter is not installed. Please install it and try again. brew install python-tk")
    
    # Declare the main script
    project.set_property('distutils_console_scripts', ['python-jira-crawler=main:main'])
