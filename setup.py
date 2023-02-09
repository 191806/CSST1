import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="dwarf",
    version="1.0",
    author="Shi Ruifeng",
    author_email="shiruifeng@mail.ynu.edu.cn",
    description="A package to estimate metallicity of dwarf stars from CSST filter systems",
    long_description=long_description,
#    long_description_content_type="text/markdown",
    url="https://github.com/191806/CSST1",
    packages=setuptools.find_packages(),
    # 模块相关的元数据
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    install_requires=[
        'numpy','pandas','glob','os'
    ],
    python_requires='>=3',
)
