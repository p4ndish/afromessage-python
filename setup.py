from setuptools import setup, find_packages
import os

# Read README.md
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='afromessage_service',
    version='0.1.0',
    author='p4ndish',
    author_email='tesfayedagim5@gmail.com',
    description='A wrapper around afromessage SMS service',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/p4ndish/afromessage_service',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    install_requires=[
        'httpx',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0.0',
            'pytest-cov>=2.10.0',
            'flake8>=3.8.0',
            'black>=20.8b1',
            'twine'
        ],
    }
)


