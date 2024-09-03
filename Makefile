api-gateway:
	python main.py &


run: api-gateway
	echo runing
	
test_app: export SETTINGS=settings.test
test_app:
	pytest -v . 
	rm test.sqlite3

tear_down:
	killall python
