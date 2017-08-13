.PHONY: penv test pkg

all: penv test pkg

penv:
	vitualenv python --no-download
	. python/bin/activate
	pip install -i http://pypi.douban.com/simple --trusted-host -r requirement.txt

test:
	. python/bin/activate
	nosetests

pkg:
	tar czvf ci.pgz ../*

clean:
	rm -r ci.pgz
