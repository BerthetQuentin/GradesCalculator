from setuptools import setup, find_packages

setup(
    name='GradesCalculator',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'GradesCalculator=GradesCalculator.main:main',
        ],
    },
    author='Quentin Berthet',
    author_email='quentin@berthet.ch',
    description='Un package pour calculer des notes avec des poids différent.',
    url='https://github.com/BERTHETquentin/GradesCalculator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
