from setuptools import setup, find_packages
from codecs import open
from os import path

#try: # for pip >= 10
#    from pip._internal.req import parse_requirements
#    from pip._internal import download
#except ImportError: # for pip <= 9.0.3
#    from pip.req import parse_requirements
#    from pip import download
    
    
# add
import pip
pip_major_version = int(pip.__version__.split(".")[0])
if pip_major_version >= 20:
    from pip._internal.req import parse_requirements
    from pip._internal.network.session import PipSession
elif pip_major_version >= 10:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
else: # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession
    

install_reqs = parse_requirements("requirements.txt", session=  PipSession())
#install_requires = [str(ir.req) for ir in install_reqs]

#requirements = [str(ir.req) for ir in install_reqs]    
#requirements = list(requirements) 
try:
    install_requires = [str(ir.req) for ir in install_reqs]
except:
    install_requires = [str(ir.requirement) for ir in install_reqs]
    
#install_reqs = parse_requirements("requirements.txt", session=download.PipSession())
#install_requires = [str(ir.req) for ir in install_reqs]


here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='textclustering',
    version='1.0.0',

    description='',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/Ashail33/textclustering',

    # Author details
    author='lvwerra Leandro von Werra',
    # author_email=''

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords='clustering of text',

    packages=find_packages(),

    install_requires=install_requires
)
