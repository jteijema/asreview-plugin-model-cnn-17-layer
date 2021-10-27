from setuptools import setup
from setuptools import find_namespace_packages

setup(
    name='asreview-plugin-model-cnn-17-layer',
    version='0.1.1',
    description='The plugin that adds a new cnn classifier',
    url='https://github.com/JTeijema/asreview-plugin-model-cnn-17-layer',
    author='ASReview team, Jelle Teijema',
    author_email='j.j.teijema@gmail.com',
    classifiers=[
        'Development Status :: 1 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='systematic review',
    packages=find_namespace_packages(include=['asreviewcontrib.*']),
    python_requires='~=3.6',
    install_requires=[
        'sklearn',
        'asreview>=0.13',
        'tensorflow',
        'scipy'
    ],
    entry_points={
        'asreview.models.classifiers': [
            'power_cnn = asreviewcontrib.models.cnn:POWER_CNN',
        ],
        'asreview.models.feature_extraction': [
            # define feature_extraction algorithms
        ],
        'asreview.models.balance': [
            # define balance strategy algorithms
        ],
        'asreview.models.query': [
            # define query strategy algorithms
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/JTeijema/asreview-plugin-model-cnn-17-layer/issues',
        'Source': 'https://github.com/JTeijema/asreview-plugin-model-cnn-17-layer',
    },
)
