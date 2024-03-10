
from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT='-e .'
## metadata info about the entire project

def get_requirements( file_path: str ) -> List[str]:
    '''
    this function return the list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file_obj: ## WE CAN ALSO MENTION ANY FILE PATH instead of requirements.txt
        requirements=file_obj.readlines() ## whenever lines get added or read the \n also gets read so we will replace that \n with a space, writing a list comprehension
        requirements=[req.replace("\n"," ") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
    
setup(
    name='mlproject',
    version='0.0.1',
    author='Somya',
    author_email='sharma.somya1100@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )

