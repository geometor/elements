from setuptools import setup, find_packages

setup(
    name='geometor.elements',
    version='0.1.0',
    #  py_modules=['logger'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'textual',
    ],
    entry_points={
        'console_scripts': [
            'logger = photonplatform.logger',
        ],
    },
)

