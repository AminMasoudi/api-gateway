api-gateway:
	python main.py &

admin:
	python admin.py &

run: admin api-gateway
	echo runing
	
test_app: export SETTINGS=settings.dev
test_app:
	pytest -v . 

tear_down:
	killall python