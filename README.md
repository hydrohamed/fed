# Flood Events Database

Flood Events Database is a free, open-source web application that allows users to view and track flood events around the world. The website gathers data from public sources, news websites, social media, voluntary researchers, and other free resources. It is built using Django and provides an interactive global map where users can click on markers to view detailed information about each flood event. Registered users have the capability to add and edit flood event data.

## Features

- **Interactive Global Map**: View flood event locations worldwide.
- **Flood Event Details**: Click on markers to view detailed information about each flood event.
- **Community Sourced**: Data is gathered from public sources, news websites, social media, and voluntary researchers.

## Installation

### Prerequisites

- Docker
- Docker Compose

### Steps

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/global-flood-events-tracker.git
    cd global-flood-events-tracker
    ```

2. **Build and start the containers**

    ```bash
    docker-compose up --build
    ```

3. **Create a superuser**

    Open a new terminal and run:

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

4. Open your web browser and navigate to `http://127.0.0.1:8000/` to see the application in action.

## Usage

- **Index Page**: Displays a global map with markers indicating flood event locations.
- **Flood Event Details**: Click on a marker to view more details about the flood event.
- **Admin Panel**: Access the Django admin panel at `http://127.0.0.1:8000/admin/` to add, edit, and manage flood events.

## Development

### Running tests

To run tests inside the Docker container, use the following command:

```bash
docker-compose exec web python manage.py test
```
## Usage

- **Index Page**: Displays a global map with markers indicating flood event locations.
- **Flood Event Details**: Click on a marker to view more details about the flood event.
- **Admin Panel**: Access the Django admin panel at `http://127.0.0.1:8000/admin/` to add, edit, and manage flood events.

## Contributing

We welcome contributions from the community! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Submit a pull request.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project uses data gathered from public sources, news websites, social media, voluntary researchers, and other free resources.
- Built with Django.

## Contact

For any inquiries, please contact us at [samsami.hd@gmail.com](mailto:samsami.hd@gmail.com).

