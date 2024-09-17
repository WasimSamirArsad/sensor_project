from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e."

def get_requirements(file_path:str)->list[str]:
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)    

    return requirements

setup(
    name="fault detection",
    version="0.0.1",
    author="wasim akhtar",
    author_email="wasimcode12091@gmail.com",
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)