from setuptools import setup, find_packages


with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name='testlib',
    version='0.0.12',

    descritption="A test CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    package_dir={'': 'src'},
    packages=find_packages(where="src"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-s3",
        "aws-cdk.aws-sns"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: GNU General Public License v3.0",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)