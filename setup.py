#! /usr/bin/python
from setuptools import setup

# to install type:
# python setup.py install --root=/
def readme():
    with open('README.md') as f:
        return f.read()
        
setup (name='PyArabic', version='0.6.5',
      author='Taha Zerrouki',
      author_email='taha_zerrouki@hotmail.com',
      url='http://pyarabic.sourceforge.net/',
      license='GPL',
      description="Arabic text tools for Python",
      long_description = readme(),
      long_description_content_type='text/markdown',
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
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Text Processing :: Linguistic',
          ],
    );

