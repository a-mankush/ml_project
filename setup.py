from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> list[str]:
    """
    This function returns lists of requirements.

    """
    requirements: list[str] = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        print(requirements)

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="mlProject",
    version="0.0.1",
    author="Aman Kumar Kushwaha",
    author_email="amansom155@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
