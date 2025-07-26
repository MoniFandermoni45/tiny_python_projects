#!/usr/bin/env python3
"""tests for hello.py"""

import os
from subprocess import getstatusoutput, getoutput
import platform

prg = './hello.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_runnable():
    """Runs using python3"""

    out = getoutput(f'python3 {prg}')
    assert out.strip() == 'Hello, World!'


# --------------------------------------------------
def test_executable():
    """Says 'Hello, World!' by default"""

    # out = getoutput(prg)
    if platform.system() == 'Windows':
        cmd = 'python hello.py'
    else:
        cmd = prg
    out = getoutput(cmd)
    assert out.strip() == 'Hello, World!'


# --------------------------------------------------
def test_usage():
    """usage"""

    # needs to be corrected
    if platform.system() == 'Windows':
        cmd = 'python hello.py'
    else:
        cmd = prg

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{cmd} {flag}')
        assert rv == 0 # assert that code is 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_input():
    """test for input"""

    if platform.system() == 'Windows':
        cmd = 'python hello.py'
    else:
        cmd = prg

    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f'{cmd} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'
