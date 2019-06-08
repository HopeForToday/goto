from setuptools import setup

setup(
    name="goto",
    version="0.1",
    py_modules=["goto"],
    install_requires=["Click", "commentjson"],
    entry_points="""
        [console_scripts]
        goto=goto:cli
    """,
)
