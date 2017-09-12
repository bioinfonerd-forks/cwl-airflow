from setuptools import setup, find_packages
import os

setup(
    name='cwl-airflow',
    description='Python package to extend Airflow functionality with CWL v1.0 support',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    version='0.0.1',
    url='https://github.com/Barski-lab/cwl-airflow',
    download_url=('https://github.com/Barski-lab/cwl-airflow'),
    author='Michael Kotliar',
    author_email='misha.kotliar@gmail.com',
    license = 'MIT',
    packages=find_packages(),
    install_requires=[
        'cwltool==1.0.20170622090721',
        'jsonmerge',
        'mysql-python>=1.2.5',
        'ruamel.yaml<0.15',
        "airflow==1.8.0",
        "html5lib"
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            "airflow-cwl-runner=cwl_runner.main:main",
            "cwl-runner=cwl_runner.main:main"
        ]
    }
)