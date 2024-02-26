from setuptools import setup, find_packages

setup(
    name='chatgptcli',
    version='0.1.0',
    packages=find_packages(),
    py_modules=['app'],
    install_requires=[
        
    ],
    entry_points={
        'console_scripts': [
            'gpt=app:main'
        ],
    }
)
