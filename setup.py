from distutils.core import setup

with open('LICENSE') as f:
    license = f.read()

with open('README.rst') as f:
    readme = f.read()


setup(
    name='crypto',
    version='0.1.0',
    packages=[''],
    url='github.com/aburgd/crypto',
    long_description=readme,
    license=license,
    author='Alec Burgdorf',
    author_email='aeburgd@gmail.com',
    description=''
)
