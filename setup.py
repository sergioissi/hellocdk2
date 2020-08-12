from setuptools import setup, find_packages


with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name='testlib',
    version='0.0.12',

    long_description=long_description,
    long_description_content_type="text/markdown",

    package_dir={'testlib': 'src'},
    packages=find_packages(where="src/testlib"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-s3",
        "aws-cdk.aws-sns"
    ],

    python_requires=">=3.6",

)

setup(
    name='devopscdk',
    version='0.0.2',

    long_description=long_description,
    long_description_content_type="text/markdown",

    package_dir={'devopscdk': 'src'},
    packages=find_packages(where="src/devopscdk"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-lambda"
    ],

    python_requires=">=3.6",
)
