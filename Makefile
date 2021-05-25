bootstrap:
	pip install virtualenv
	pip install --upgrade virtualenv
	virtualenv env
	. env/bin/activate
	pip install -r requirement.txt