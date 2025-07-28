from setuptools import setup, find_packages

HYPEN_E_DASH = '-e .'

def get_requirements(requirements_file:str) -> list:
    """
    This function reads a requirements file and returns a list of requirements.
    
    :param requirements_file: Path to the requirements file
    :return: List of requirements
    """
    with open(requirements_file, 'r') as file:
        requirements= [line.strip() for line in file if line.strip() and not line.startswith('#')]
    if HYPEN_E_DASH in requirements:
        requirements.remove(HYPEN_E_DASH)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Anouar',
    author_email='kherchoucheanouar98@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(requirements_file='requirements.txt'))