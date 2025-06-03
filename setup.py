from setuptools import find_packages, setup
from typing import List

HYPEN_DOT_E="-e ."
def get_requirments(file_path: str)->List[str]:
    '''
    this functions will return the list of  requirment 
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments =file_obj.readlines()
        requirments=[req.replace(("\n"), "") for req in requirments]
        
        if HYPEN_DOT_E in requirments:
            requirments.remove(HYPEN_DOT_E)
    return requirments

setup(
    name='mlpProject',
    version='0.0.1',
    author='Ali Raza',
    author_email='mianaliraza29437815@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')
)
