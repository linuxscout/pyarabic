#/usr/bin/sh
# Build pyArabic package

default: all
# Clean build files
clean:
	
backup: 
	
#create all files 
all: 

# Publish to github
publish:
	git push origin master 

md2rst:
	pandoc -s -r markdown -w rst README.md -o README.rst
md2html:
	pandoc -s -r markdown -w html README.md -o README.html
	
wheel:
	sudo python setup.py bdist_wheel
sdist:
	sudo python setup.py sdist
upload:
	echo "use twine upload dist/PyArabic-0.6.1.tar.gz"
	
test:
	pytest pyarabic/test_araby.py
