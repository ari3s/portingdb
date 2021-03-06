
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        super().finalize_options()
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


requires = [
    'sqlalchemy >= 1.0, < 2.0',
    'PyYAML >= 3.11, < 4.0',
    'click >= 3.3, < 7.0',
    'flask >= 0.10, < 1.0',
    'markdown >= 2.4, < 3.0',
    'dogpile.cache >= 0.5.5, < 1.0',
    'taskotron-python-versions >= 0.1.dev2',
]

tests_require = ['pytest']

setup_args = dict(
    name='portingdb',
    version='0.1',
    packages=['portingdb'],
    url='https://github.com/fedora-python/portingdb',

    description="""Database of packages that need Python 3 porting""",
    author='Petr Viktorin',
    author_email='pviktori@redhat.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    install_requires=requires,

    tests_require=tests_require,
    cmdclass={'test': PyTest},

)


if __name__ == '__main__':
    setup(**setup_args)
