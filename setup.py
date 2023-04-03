from setuptools import setup, find_packages
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))
setup(
    name='ljctoolbox',
    version='0.0.1',
    # packages=['ljctoolbox','ljctoolbox.mjson'],
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    package_dir={'ljctoolbox': 'ljctoolbox'},
    description='Ljc tool box',
    # The project's main homepage.
    # url='opconty - Overview',
    # Author details
    author='ljc',
    author_email='liujichao.ljc@qq.com',
    # Choose your license
    license='GPLv3',
    python_requires='<=3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    py_modules=["algorithm","file_parser","process_pool","thread_pool", "timebox"]
)