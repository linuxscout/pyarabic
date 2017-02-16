#! /usr/bin/python
from setuptools import setup

# to install type:
# python setup.py install --root=/
def readme():
    with open('README.rst') as f:
        return f.read()
        
setup (name='PyArabic', version='0.6.2',
      author='Taha Zerrouki',
      author_email='taha_zerrouki@hotmail.com',
      url='http://pyarabic.sourceforge.net/',
      license='GPL',
      description="Arabic text tools for Python",
      long_description = readme(),
      package_dir={'pyarabic': 'pyarabic',},
      packages=['pyarabic'],
      package_data = {
        'pyarabic': ['doc/*.*','doc/html/*'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Natural Language :: Arabic',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Text Processing :: Linguistic',
          ],
    );

