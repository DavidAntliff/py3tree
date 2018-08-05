import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py3tree",
    version="0.0.1",
    author="David Antliff",
    author_email="david.antliff@gmail.com",
    description="Display the i3 tree for the current or all workspaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DavidAntliff/py3tree.git",
    packages=setuptools.find_packages(),
    install_requires=[
        "future>=0.16.0",
        "i3ipc>=1.5.1",
    ],
    entry_points={
        'console_scripts': [
            'py3tree = py3tree.py3tree:main'
        ]
    },
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Environment :: X11 Applications",
        "Topic :: Desktop Environment :: Window Managers",
        "Operating System :: OS Independent",
    ),
)
