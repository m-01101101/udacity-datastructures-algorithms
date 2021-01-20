"""
 the goal is to write code for finding all files under a directory
 (and all directories beneath it) that end with ".c"

 os.walk() is a handy Python method which can achieve this task very easily.
 However, for this problem you are not allowed to use os.walk()
 """

import pathlib
import pytest
from typing import List


def find_files(suffix: str, path: str) -> List[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == "":
        raise ValueError("must provide suffix for file types to be returned")

    files = list()
    p = pathlib.Path(path)
    files = [f for f in p.iterdir() if f.suffix == suffix and f.is_file()]

    for x in p.iterdir():
        if x.is_dir():
            p = x
            files.extend(find_files(suffix, p))

    return files


c_files = find_files(".c", "testdir")
h_files = find_files(".h", "testdir/subdir1")

assert len(c_files) == 4
assert len(h_files) == 1


def test_suffix_exception():
    with pytest.raises(Exception):
        assert find_files("", "testdir")  # do not accept no suffix
