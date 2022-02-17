from setuptools import setup
import ndi
from os import path

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


# Open the peripheral files and load into ram
installReqs = [n.requirement for n in parse_requirements('requirements.txt', session='hack')]
longdesc = None
with open('./README.md', 'r') as handle:
    longdesc = handle.read()

# Main setuptools initialization
setup(
    name='PyNDI',
    version=ndi.__version__,
    description='A very simple Python wrapper for NewTek NDI using CFFI.',
    long_description=longdesc,
    long_description_content_type='text/markdown',
    author='labrat97',
    author_email='james@nineseven.net',
    url='https://github.com/labrat97/pyNDI',
    packages=['ndi'],
    package_data={'ndi': [f'ndi{path.sep}bin']},
    package_dir={'ndi': 'ndi'},
    install_requires=installReqs
)
