from pybuilder.core import init, task, use_plugin

use_plugin("python.core")                 # basic build of files 
use_plugin("python.install_dependencies") # to be able to install dependencies (like mockito) via command < pyb install_dependencies >
use_plugin("python.unittest")             # to be able to run unit tests. Use < pyb -v > for mopre info
use_plugin("python.coverage")             # to be able to check test coverage and fail by default if less than 70%
use_plugin("python.distutils")            # to be able to install the package via <python setup.py install>
use_plugin('python.pycharm')              # PyCharm generate project files
use_plugin('python.pydev')                # PyDev generate project files

default_task = "publish"

name = "python-sandbox"
version = "1.0"

summary = "Basic python application to show tools, infrastructure, python basics"
license = "Apache Software License"

url = "https://github.com/Iurii-Dziuban/python3-sandbox"

@init
def initialize(project):                  # initialize dependencies, project version, properties, licence, etc.
    project.set_property('unittest_module_glob', '*_tests') #convension over configuration. Configured by default. Only for demo
    project.set_property('coverage_break_build', True)
    project.set_property("coverage_threshold_warn", 100)
    project.set_property("coverage_branch_threshold_warn", 100)
    project.set_property("coverage_branch_partial_threshold_warn", 100)
    project.build_depends_on('mockito')
    project.build_depends_on('coverage')

# test task execution with the following command <pyb_ say_hello -Pspam="spam message">	
@task("say_hello", description="task example")
def say_hello (logger, project):          # dependency injection for "logger" and "project"
    print (project.get_property('spam'))
    print ("Hello, PyBuilder")
    logger.info("I am building {0} in version {1}!".format(project.name, project.version))
    pass