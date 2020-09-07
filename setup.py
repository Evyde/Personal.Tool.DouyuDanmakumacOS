from setuptools import setup, find_packages
from pathlib import Path

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    name="Douyu_Danmaku_For_macOS",
    version="0.0.1",
    author="Evyde HF",
    python_requires=">3.7.0",
    author_email="life.app.hanfeng@hotmail.com",
    description="A danmaku assistant for macOS.",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/ForeverOpp/Douyu_Danmaku_For_macOS",
    packages=find_packages(),
    install_requires=[
        "danmaku",
        "aiohttp"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
    ],
)