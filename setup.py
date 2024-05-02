from setuptools import setup, find_packages

setup(
    name='spacyex',
    version='0.0.1',
    author='William J.B. Mattingly',
    description='An extension for spaCy, making pattern matching as flexible as using regular expressions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wjbmattingly/spacyex',
    packages=find_packages(),
    install_requires=[
        'spacy>=3.5'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    include_package_data=True
)
