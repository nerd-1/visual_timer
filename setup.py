from distutils.core import setup

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(
    name='visual_timer',  
    version='0.1',
    scripts=['visual_timer'] ,
    author="nerd1",
    authoremail="nerd1pypi@cock.li"
    description="Visual timer is a simple terminal based timer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nerd-1/visual_timer",
    keywords=["timer","ui"]
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python"
        "Programming Language :: Python :: 3",
        "Development Status :: 0.1 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Other/Nonlisted Topic",
        "Enviroment :: Curses"
    ],
)
