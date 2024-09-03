api-gateway:
	python main.py


deploy: export SETTINGS=settings.prod
deploy: test_app api-gateway
	@echo deploy
	
test_app: export SETTINGS=settings.test
test_app:
	pytest -v . 
	rm -f test.sqlite3

tear_down:
	killall python
