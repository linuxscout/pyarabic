#/usr/bin/sh
# Build pyArabic package

default: all
# Clean build files
clean:
	
backup: 
	
#create all files 
all: 

install:
	sudo python setup.py install
install3:
	sudo python3 setup.py install
# Publish to github
publish:
	git push origin master 

md2html:
	pandoc -s -r markdown -w html README.md -o README.html
	
wheel:
	sudo python setup.py bdist_wheel
wheel3:
	sudo python3 setup.py bdist_wheel
sdist:
	sudo python setup.py sdist
upload:
	echo "use twine upload dist/PyArabic-0.6.1.tar.gz"
	
test:
	python -m unittest discover tests
doc:
	epydoc -v --config epydoc.conf
