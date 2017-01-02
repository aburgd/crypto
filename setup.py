from distutils.core import setup


setup(
    name='crypto',
    version='0.1.0',
    packages=[''],
    url='github.com/aburgd/crypto',
    long_description=readme,
    license=license,
    author='Alec Burgdorf',
    author_email='aeburgd@gmail.com',
    description='a python module for generating DHKE integer keys'
    long_description='This Python module is a demonstration'
                     'of the Diffie-Hellman(-Merkle)'
                     'Key Exchange algorithm, used to derive public keys and'
                     'shared secrets for parties in a cryptographic system.'
)
