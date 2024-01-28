# PHISHGUARD

## Installation and Setup

### Prerequisites
- **Git**: Make sure Git is installed on your system for cloning the repository.
- **Docker**: Ensure Docker is installed on your system for running the application.

### Steps
1. **Clone the repository**:
    - Clone the "phishguard" project repository to your local machine:
        ```bash
        git clone https://github.com/IvanGeorgievProgramming/phishguard.git
        ```	
    - Navigate to the project directory:
        ```bash
        cd phishguard
        ```
2. **Set Up Environment Variables**:
    - Create a `.env` file in the root directory of the project:
        ```bash
        cp .env.example .env
        ```
    - Edit the `.env` file with your specific settings:
      - Replace `your_secret_key_here` with a secure key.
      - Set `EMAIL_SENDER` and `EMAIL_PASSWORD` to your email credentials.
3. **Build the Docker Image**:
    - Create a Docker image named `phishguard`:
        ```bash
        docker build -t phishguard .
        ```
4. **Run the Docker Container**:
    - Start a container from the `phishguard` image:
        ```bash
        docker run -p 5000:5000 --name phishguard_container --rm phishguard
        ```
    - This command runs the container, making your application accessible on port 5000. The `--name` option names your container `phishguard_container`, and the `--rm` flag automatically removes the container when it exits.

### Accessing the Application
- Open your web browser and navigate to `http://localhost:5000` to access the "PHISHGUARD" application.
