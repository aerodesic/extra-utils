from DistUtilsExtra.auto import setup
from distutils.command.install import install
import os

PACKAGE="extra"
VERSION="1.0"

# In case we need hooks
class post_install(install):
    def run(self):
        install.run(self)

setup(
    name              = PACKAGE,
    author            = "Gary Oliver",
    author_email      = "go@aerodesic.com",
    url               = "http://aerodesic.com",
    version           = VERSION,
    packages          = [ "extra" ],
    license           = "Copyright 2018-2021, Gary Oliver",
    description       = "Miscellaneous Useful Utilities",
    long_description  = open("README.md").read(),
    cmdclass          = { 'install': post_install },
)
