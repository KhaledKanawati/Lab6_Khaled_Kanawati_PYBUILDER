from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.distutils")

name = "calculator_Khaled_Kanawati"
version = "0.1"
default_task = "publish"


@init
def initialize(project):
    project.set_property("dir_source_unittest_python", "tests/unittest/calculator_Khaled_Kanawati")
    project.set_property("unittest_module_glob", "test_*")
