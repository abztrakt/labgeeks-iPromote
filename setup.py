from setuptools import setup

setup(
    name = 'labgeeks-iPromote',
    version = '0.1',
    license = 'Apache',
    url = 'http://github.com/abztrakt/labgeeks_iPromote',
    description = 'The promotion track app for the labgeeks suite of student staff management tools.',
    author = 'Craig Stimmel',
    packages = ['labgeeks_iPromote',],
    install_requires = [
        'setuptools',
        'labgeeks-people',
        'South==0.7.3',
    ],
)
