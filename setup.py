from setuptools import find_packages, setup

VERSION = "0.2.01"
DESCRIPTION = ""
LONG_DESCRIPTION = ""

setup(
    name="parse-le-beacon",
    version=VERSION,
    author="Thyrasec",
    url="https://github.com/thyrasec/parse-le-beacon",
    author_email="",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[        
    ],  # add any additional packages that
    # needs to be installed along with your package
    keywords=["python"],
    classifiers=[],
    entry_points={
        'console_scripts': ['<parse-le-beacon> = <parse-le-beacon>.console:main'],
    }
)