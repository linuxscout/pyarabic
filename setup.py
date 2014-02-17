#! /usr/bin/python
from distutils.core import setup
from glob import glob

# to install type:
# python setup.py install --root=/

setup (name='PyArabic', version='0.4',
      description='pyarabic Arabic text tools for Python',
      author='Taha Zerrouki',
      author_email='taha_zerrouki@gawab.com',
      url='http://pyarabic.sourceforge.net/',
      license='GPL',
      #Description="Arabic Arabic text tools for Python",
      #Platform="OS independent",
      package_dir={'pyarabic': 'pyarabic',},
      packages=['pyarabic'],
      # include_package_data=True,
      package_data = {
        'pyarabic': ['doc/*.*','doc/html/*'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
    );

