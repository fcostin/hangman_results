all:
	python build_index.py
.PHONY: all

clean:
	rm -rf index.html
.PHONY: clean
