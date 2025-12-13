from setuptools import find_packages, setup
from typing import List

IGNORED_PREFIXES = ("-e", "--", "git+", "file:")

def get_requirements(file_path: str) -> List[str]:
    """
    Read requirements.txt and return a cleaned list suitable for install_requires.
    Filters out pip options and editable/local path entries like '-e .'.
    """
    reqs: List[str] = []
    with open(file_path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if any(line.startswith(prefix) for prefix in IGNORED_PREFIXES):
                continue
            reqs.append(line)
    return reqs

setup(
    name="MLPROJECT",
    version="0.0.1",
    author="anuj",
    author_email="anuj.jakhar.2104@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)