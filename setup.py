from setuptools import find_packages,setup
from typing import List

"""HYPEN_E_DOT='-e .'

# this function will read the requirements.txt file and return the list of requirements
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements"""

setup(
    name='DimondPricePrediction',
    version='0.0.0',
    author='Yash Pathak',
    author_email='7Ai@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()  # this will find the local packages in local dpythirectory
    #Example: packages=find_packages(where="src") # this will find the local packages in src directory
)