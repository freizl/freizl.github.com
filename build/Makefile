PD=pandoc

.PHONY: slides

default: build

clean:
	rm -rf _site
	stack exec freizl clean

build:
	stack build

install:
	stack install

run:
	stack exec freizl watch

########## Mirror to github

deploy:
	stack exec freizl build
	cp -r _site/* ../

########## Compile slides

## just being lazy not to cut off md file ext.
slides:
	for f in `ls -1 slides/*.md`; do \
	$(PD) -t dzslides -s "$$f" -o "$$f".html; \
	done;
