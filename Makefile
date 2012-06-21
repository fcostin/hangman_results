all:	index.html
.PHONY: all

clean:
	rm -rf *.html
.PHONY: clean

publish: index.html
	./publish.sh
.PHONY: publish

index.html:	index.html.template result_database.py
	python build_index.py

%.html:	%.markdown
	cat $^ | markdown > $@
