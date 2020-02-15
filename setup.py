from setuptools import setup

setup(
    name='mkdocs-lilypond',
    version='0.0.1',
    packages=['mkdocs_lilypond'],
    url='https://github.com/uliska/lilypond-mkdocs-plugin',
    license='GPL',
    author='Urs Liska',
    author_email='git@ursliska.de',
    description='LilyPond support for MkDocs.',
    install_requires=['mkdocs', 'python-ly'],

    # The following rows are important to register your plugin.
    # The format is "(plugin name) = (plugin folder):(class name)"
    # Without them, mkdocs will not be able to recognize it.
    entry_points={
        'mkdocs.plugins': [
            'lilypond = mkdocs_lilypond:LilyPond',
        ]
    },
)
