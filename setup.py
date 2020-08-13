from setuptools import setup, find_packages


with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name='devopscdk',
    version='0.0.3',

    long_description=long_description,
    long_description_content_type="text/markdown",

    package_dir={'': 'src'},
    packages=find_packages(where="src"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-lambda"
    ],

    python_requires=">=3.6",
)
