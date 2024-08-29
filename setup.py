from setuptools import find_packages,setup


hyphen_e_dot = '-e .'

def get_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if not line.startswith('#') and line.strip() != hyphen_e_dot]

    


# metadata information about the project
setup(
    name='mlproject',
    version='0.0.1',
    author='Mohamed',
    author_email='mohamedgamal1001000@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='Machine Learning Project',
    long_description='A project to explore machine learning algorithms.'
)