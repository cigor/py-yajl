import os
from distutils.core import setup, Extension

base_modules = [
    Extension('yajl',  [ 
                'yajl.c',
                'encoder.c',
                'decoder.c',
                'yajl/src/yajl_alloc.c',
                'yajl/src/yajl_buf.c',
                'yajl/src/yajl.c',
                'yajl/src/yajl_encode.c',
                'yajl/src/yajl_gen.c',
                'yajl/src/yajl_lex.c',
                'yajl/src/yajl_parser.c',
            ],
            include_dirs=('.', 'includes/', 'yajl/src'),
            extra_compile_args=['-Wall',],
            language='c'),
        ]


packages = ('yajl',)


setup(
    name = 'yajl',
    description = '''A CPython module for Yet-Another-Json-Library''',
    version = '0.2.1',
    author = 'R. Tyler Ballance',
    author_email = 'tyler@monkeypox.org',
    ext_modules=base_modules,
)

