from setuptools import setup

setup(
    name='pass_logit',
    version='0.1',
    description='Implementation of PASS-GLM for logistic regression',
    url='http://github.com/amacfie/pass_logit',
    author='Andrew MacFie',
    author_email='andrew222651@fastmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    packages=['pass_logit'],
    # 3.8 is the newest Python with wheels for numpy==1.18.0 (pinned below);
    # it's also the newest interpreter available as of Dec 2019, when this
    # project was written (released 2019-10-14)
    python_requires='>=3.8,<3.9',
    # pinned to the latest releases available as of Dec 2019, when this
    # project was written
    install_requires=[
        'pyspark==3.4.4',
        'numpy==1.18.0',
        'sympy==1.5',
        'theano==1.0.4',
        'scipy==1.4.1',
        'matplotlib==3.1.2',
        'pymc3==3.8',
        # pymc3 3.8 only declares arviz>=0.4.1 with no upper bound; pinning
        # to the version current at the time avoids pulling in a modern
        # arviz that has since dropped APIs pymc3 3.8 relies on (e.g. geweke)
        'arviz==0.6.1',
    ],
    zip_safe=False,
)
