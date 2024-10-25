#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, Author, task, after
import sys
import os

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
    project.depends_on("requests")
    project.depends_on("canvasvg")
    project.depends_on("cairosvg")
    
    # Check for tkinter
    try:
        import tkinter
    except ImportError:
        sys.exit("Error: tkinter is not installed. Please install it and try again. brew install python-tk")
    
    # Declare the main script
    project.set_property('distutils_console_scripts', ['python-jira-crawler=main:main'])
    
    
    # Set unittest properties
    project.set_property('unittest_module_glob', '*_test')
    project.set_property('unittest_verbosity', 2)  # Increase verbosity to show test names
    project.set_property('unittest_break_at_fail', True)  # Stop at first failure

@after('run_unit_tests')
#@finalizer
def unit_test(project, logger):
    with open('target/reports/unittest', 'r') as file:
        print(file.read())
