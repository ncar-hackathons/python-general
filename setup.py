from setuptools import setup, find_packages
import os
import os.path as op
from glob import glob
from python_general import __version__

# Location of the template files we use for cloning
template_files = glob(
    op.join('python_general', 'book_template', '**', '*'), recursive=True)
template_files += glob(op.join('python_general', 'minimal',
                               '**', '*'), recursive=True)
template_files = [ii.replace('python_general' + os.sep, '', 1)
                  for ii in template_files]
PACKAGE_DATA = {"python_general": template_files}

# Source dependencies from requirements.txt file.
with open('requirements.txt', 'r') as f:
    lines = f.readlines()
    install_packages = [line.strip() for line in lines]

setup(
    name='python-general',
    use_scm_version={'version_scheme': 'post-release', 'local_scheme': 'dirty-tag'},
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0'],
    install_requires=install_packages,
    python_requires='>=3.6',
    maintainer='Anderson Banihirwe',
    maintainer_email='abanihi@ucar.edu',
    url='',
    # this should be a whitespace separated string of keywords, not a list
    keywords="reproducible science environments scholarship notebook NCAR",
    description="fundamentals of Python programming language.",
    license='BSD',
    packages=find_packages(),
    use_package_data=True,
    package_data=PACKAGE_DATA,
    entry_points={
        'console_scripts': [
            'jupyter-book = python_general.main:main',
        ]
    },
)
