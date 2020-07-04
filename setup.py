from setuptools import setup, find_packages


setup(
    name="rever-python-logger",
    version="0.1.0",
    url="http://github.com/reverscore/rever-python-logger",
    license="MIT",
    description="Logger library used in Rever",
    install_requires=open('requirements.txt').read().splitlines(),
    author="Luis Elizondo",
    author_email="noreply@reverscore.com",
    package_dir={'': 'src'},
    packages=find_packages("src", exclude="tests"),
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires='>=3.4',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Logging',
    ]
)
