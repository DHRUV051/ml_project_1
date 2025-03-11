from typing import List
from setuptools import find_packages, setup

HYPEN_E_DOT='-e .'

def get_requirements(file_name)->List[str]:
    """"
    get_requirements function is used to get all the requirements from requirements.txt 
    and return list of this requirements.
    """
    
    requirements = []
    
    with open(file_name) as file:
        requirements = file.readlines()
        requirements = [req.replace("/n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
    

setup(
    name='mlproject',
    version='0.0.1',
    author='Dhruv',
    author_email='dhruvparmar051@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)