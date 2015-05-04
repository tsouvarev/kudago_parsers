from setuptools import setup


setup(
    name='kudago_parsers',
    packages=['kudago_parsers'],
    version='1.0',
    description='Parsers for KudaGo',
    author='Ivan Tsouvarev',
    author_email='tsouvarev@mail.ru',
    url='https://github.com/tsouvarev/kudago_parsers',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Testing',
    ],
    install_requires=[
        'Django>=1.8',
    ]
)