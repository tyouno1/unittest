.PHONY: penv test pkg

all: penv test pkg

penv:
	virtualenv python --no-download
	. python/bin/activate; pip install -i https://pypi.douban.com/simple -r requirements.txt

test:
	. python/bin/activate; nosetests

pkg:
	tar czvf ci.pgz ../*

clean:
	rm -r ci.pgz
	rm -rf python
