from setuptools import setup, find_packages

from briefme_indexable_feed import __version__

setup(
    name="briefme-indexable-feed",
    version=__version__,
    description="indexable-feed base for Brief.me projects",
    url="https://github.com/briefmnews/briefme-indexable-feed",
    author="Brief.me",
    author_email="tech@brief.me",
    packages=find_packages(exclude="tests"),
    python_requires=">=3.7",
    install_requires=["Django>=2.2", "djangorestframework>=3.10.0", "bleach>=3.2"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
    zip_safe=False,
)
