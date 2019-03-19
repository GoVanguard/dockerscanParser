import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dockerscanParser",
    version="0.1.0",
    author="Shane Scott",
    author_email="sscott@gvit.com",
    description="Parse Dockerscan report issues into lists of dictionaries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GoVanguard/dockerscanParser",
    packages=['dockerscanParser'],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ),
)
