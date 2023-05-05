from setuptools import setup, find_packages

setup(
    name='scrapetron',
    version='1.0.0',
    description='A library for web scraping in Python.',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'beautifulsoup4',
        'requests',
    ],
    author='Rohan',
    author_email='rohan.mbox@gmail.com',
    url='https://github.com/rohzzn/scrapetron',
)
