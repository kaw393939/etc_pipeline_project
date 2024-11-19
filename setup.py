from setuptools import setup, find_packages

setup(
    name='etl_pipeline_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'etl_pipeline=src.main:main',
        ],
    },
)
