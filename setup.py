from setuptools import setup, find_packages

setup(
    name='odr',
    version='0.0.2c',

    author="Alexandr Semenov",
    author_email="a.semenov.job@gmail.com",
    description="Odr is a very simple realisation of Dependency Injection pattern with global IoC-Container and "
                "simple decorator to inject object.",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha'
    ],
    keywords='di ioc decorator inject'
)
