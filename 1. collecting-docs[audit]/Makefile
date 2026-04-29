.PHONY: create-practice remove-practice create-stucture install-dep install test-pytest test check-requirements

create-practice:
ifndef NAME
	$(error NAME is not defined)
endif
	mkdir -p $(NAME)

create-structure:
ifndef NAME
	$(error NAME is not defined)
endif
	mkdir -p $(NAME)/src
	mkdir -p $(NAME)/tests
	mkdir -p $(NAME)/docs
	touch $(NAME)/src/.gitkeep $(NAME)/tests/.gitkeep $(NAME)/docs/DOMAIN.md README.md
	touch $(NAME)/setup.py $(NAME)/requirements.txt

install-dep:
	pip install -r $(NAME)/requirements.txt

install:
	pip install -e

test-pytest:
	$(NAME)
	python3 -m pytest

test: $(NAME) install-dep install test-pytest

check-requirements:
	pip install pipreqs
	pipreqs $(NAME)

remove-practice:
ifndef NAME
	$(error NAME is not defined)
endif
	rm -rf $(NAME)

# mkdir -p makedemo/src
# mkdir -p makedemo/tests
# mkdir -p makedemo/docs