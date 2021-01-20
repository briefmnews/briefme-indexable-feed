from setuptools import setup

setup(
    name="briefme-indexable-feed",
    version="0.1",
    description="indexable-feed base for Brief.me projects",
    url="https://github.com/briefmnews/briefme-editorial",
    author="Brief.me",
    author_email="tech@brief.me",
    packages=["briefme_indexable_feed"],
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
    ],
    include_package_data=True,
    zip_safe=False,
)
