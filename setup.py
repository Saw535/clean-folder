from setuptools import setup, find_namespace_packages

setup(
    name='clean',
    version='0.1',
    description='scripts clean folder and normalize file name',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3"
      ],
    author=[],
    packages=find_namespace_packages(include=['clean_folder*']),
    install_requires=[],
    python_requires='>=3.7',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean_folder:main'
        ]
    }
)