import pathlib
import setuptools

setuptools.setup(
    name="your_project_name",
    version="your_project_version",
    description="your_project_description",
    url="your_project_url",
    long_description=pathlib.Path('README.md').read_text(),
    author="your_project_author",
    author_email="your_project_author_email",
    license="MIT License",
    python_requires=">=3.8.0, <3.9.0",
    packages=setuptools.find_namespace_packages(exclude=["example.py", "tests", "tests.*"]),
    include_package_data=True,
    install_requries=pathlib.Path('requirements.txt').read_text().splitlines(),
    extras_require={},
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)