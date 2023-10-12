all: check-style check-types fix-style localtest unittest run clean
	@echo "All done!"


run:
	python3 cosmicpathoptimization.py

unittest:
ifeq ($(shell which pytest), ) # if pytest not found
	@echo "pytest not found. Installing..."
	pip install pytest
endif
	pytest test_unit_cosmicpathoptimization.py
	@echo "All unittesting worked..."
	
localtest:
	@cat sample_data/1.in | python cosmicpathoptimization.py | diff - sample_data/1.ans
	@echo "All kattis sample data test done..."

check-types:
ifeq ($(shell which mypy), )
	@echo "mypy not found. Installing mypy..."
	pip install mypy
endif
	mypy --disallow-untyped-defs --strict cosmicpathoptimization.py
	mypy --disallow-untyped-defs --strict test_unit_cosmicpathoptimization.py
	@echo "mypy type tests passed successfully..."

check-style:
ifeq ($(shell which flake8), )
	@echo "flake8 not found. Installing flake8..."
	pip install flake8
endif
	flake8 cosmicpathoptimization.py
	flake8 test_unit_cosmicpathoptimization.py
	@echo "flake8 style tests passed successfully..."

fix-style:
ifeq ($(shell which autopep8), )
	@echo "autopep8 not found. Installing autopep8..."
	pip install autopep8
endif
	autopep8 --in-place --aggressive --aggressive cosmicpathoptimization.py
	autopep8 --in-place --aggressive --aggressive test_unit_cosmicpathoptimization.py
	@echo "autopep8 style fixed successfully... "

submit:
	kattis -f -p cosmicpathoptimization -m cosmicpathoptimization.py

clean:
	@rm -rf __pycache__
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@echo "All cleaned!"