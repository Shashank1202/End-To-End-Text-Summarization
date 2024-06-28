import setuptools

with open("README.md", "r", encoding= "utf-8")as f:
    long_description= f.read()

__version__="0.0.0"

REPO_NAME= "End-To-End-Text-Summarization"
AUTHOR_USER_NAME= "Shashank1202"
SRC_REPO= "textSummarizer"
AUTHOR_EMAIL= "shashank.s.1202@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)