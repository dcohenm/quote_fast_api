# Address Book Service

This is a FastAPI-based microservice for managing address books. It provides CRUD operations for address book entries and uses MongoDB as its database.

## Features

- Create new address book entries
- Retrieve address book entries by CUIT
- Delete address book entries
- List all address book entries

## Prerequisites

- Docker
- Python 3.9+
- MongoDB

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/YOUR_USERNAME/address-book-service.git
   cd address-book-service
   ```

2. Build the Docker image:
   ```
   docker build -t address-book-service .
   ```

3. Run the Docker container:
   ```
   docker run -d -p 8000:8000 --name address-book-container address-book-service
   ```

## Usage

The service will be available at `http://localhost:8000`. You can use tools like curl, Postman, or any HTTP client to interact with the API.

## API Endpoints

- POST /addressBook: Create a new address book entry
- GET /addressBook/{cuit}: Retrieve an address book entry by CUIT
- DELETE /addressBook/{cuit}: Delete an address book entry by CUIT
- GET /addressBooks: List all address book entries

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
