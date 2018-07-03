from setuptools import setup, find_packages

setup(
    name = 'pydlm-lite',
    version = '0.1.1.1',
    author = 'Xiangyu Wang',
    author_email = 'wwrechard@gmail.com',
    description = ('A python library for the Bayesian dynamic linear ' +
      'model for time series modeling'),
    license = 'BSD',
    keywords = 'dlm bayes bayesian kalman filter smoothing dynamic model multi-threading online',
    url = 'https://github.com/wwrechard/pydlm/tree.pydlm-lite',
    packages = find_packages(),
    classifiers = [
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    include_package_data = False,
    install_requires = [
      'numpy',
    ],
    tests_require = [
      'unittest',
    ],
    extras_require = {
        'docs': [
          'Sphinx',
        ],
        'tests': [
          'unittest',
        ],
    },
)
