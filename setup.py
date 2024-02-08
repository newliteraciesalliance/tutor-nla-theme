import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutorindigo", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-nla-theme",
    version=ABOUT["__version__"],
    url="https://github.com/newliteraciesalliance/tutor-nla-theme",
    project_urls={
        "Code": "https://github.com/newliteraciesalliance/tutor-nla-theme",
        "Issue tracker": "https://github.com/newliteraciesalliance/tutor-nla-theme/issues",
        "Documentation": "https://docs.tutor.overhang.io/",
        "Community": "https://discuss.openedx.org",
    },
    license="AGPLv3",
    author="New Literacies Alliance",
    author_email="newliteraciesalliance@gmail.com",
    maintainer="K-State Libraries",
    maintainer_email="libadm@ksu.edu",
    description="NLA theme plugin for Tutor based on Indigo",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["tutor>=17.0.0,<18.0.0"],
    entry_points={"tutor.plugin.v1": ["nla-indigo = tutorindigo.plugin"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
