import setuptools

__version__ = "0.3.0"

setuptools.setup(
    name="python_js",
    version=__version__,
    url="https://github.com/josex2r/python_js",
    author="Jose Luis Represa",
    author_email="jlrepresa@gmail.com",
    description="Some JS functions written in Python for learning purposes",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    # include static files in a package
    include_package_data=True,
    package_data={'python_js': ['python_js/py.typed']},
)
