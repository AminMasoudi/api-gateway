api-gateway:
	python main.py &

admin:
	python admin.py &

run: admin api-gateway
	echo runing
	