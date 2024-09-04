# API Gateway
## Overview
This project is an API Gateway built using **Starlette** and **HTTPX**. It is currently in the MVP stage, focusing on basic routing functionalities.

## About API gateway
check out [RedHat docs](https://www.redhat.com/en/topics/api/what-does-an-api-gateway-do) to understand the usage.

![image](https://lh5.googleusercontent.com/WSns3Ifou8w8ifxl3PTBGIvSP6UevjPdQW0PoT0zZdbwyouY1JFvYRB2Pm6Zx0eHygBK8IkkyKr6gtc4c_K56HJfMhACIWOFF4t20WpuJOof8fB7Zr4d9xeYEBQvefKRvTBfFLSOFUC05-maH_fpNTc)

## Features
- **Routing**: Directs incoming requests to the appropriate backend services.

## Planned Features
- **Dynamic Middleware:** Allows for dynamic addition and removal of middleware.
- **Firewall:** Basic firewall functionalities to secure the gateway.
- **Database Configuration:** Configures and manages database connections.
- **Observations:** Tracks and logs requests for monitoring and debugging.
- **Authentication and Authorization**: Implement security measures to control access to services.
- **Rate Limiting**: Add functionality to limit the number of requests a client can make.
- **Load Balancing**: Distribute incoming requests across multiple instances of a service.
- **Caching**: Store responses to reduce load on backend services.

## Technologies Used
**Starlette:** A lightweight ASGI framework/toolkit.
**HTTPX**: An HTTP client for Python.

## Getting Started
### Prerequisites
- Docker
### Installation
1. Clone the repository:
	```bash
	git clone https://github.com/aminmasoudi/api-gateway.git
	cd api-gateway
	```

2. Create a settings file:
	Create a file named `prod.py` in the settings directory with the necessary configuration settings.
3. Run with Docker:
	``` bash
	docker run -v $(pwd)/prod.py:/app/prod.py -p 8000:8000 aminmasoudii/api-gateway
	```


## Usage
Once the application is running, you can access the API Gateway at http://localhost:8000.

## Configuration
- **prod.py:** This file should contain all the necessary configuration settings for the application.

## Contributing
We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.

## Areas for Contribution
- **Fixing Cookies and CSRF Tokens:** Secure handling of cookies and CSRF tokens.
- **Implementing Planned Features:** Work on any of the planned features listed above.
- **Reporting any Issue**: Submit any issue you see.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or support, please contact the maintainer at aminmasoudi2003@gmail.com.
