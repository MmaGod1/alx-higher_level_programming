#!/usr/bin/python3
import builtins
builtins.__dict__['__import__']('os').write(1, b'#pythoniscool\n')
