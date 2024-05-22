# URL Word Counter

This is a Flask web application that allows users to submit URLs. The application asynchronously counts the words on the webpage of the submitted URL and displays the results. The word counts are processed using Redis Queue (RQ) and stored in MongoDB.

## Features

- Submit a URL and queue a job to count words on the webpage.
- Asynchronously process the job using Redis Queue (RQ).
- Store and display results in MongoDB.
- Dockerized for easy deployment.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose


1. **Clone the repository:**

   ```
   git clone https://github.com/<your-username>/url-word-counter.git
   cd url-word-counter
   ```

2. **Build and run the Docker containers:**

```docker-compose up --build```

3. **Access the application:**

Open your web browser and navigate to http://localhost:5000.


### Usage
1. Submit a URL:

Enter a URL in the form on the index page and click "Submit".
The job to count words at the specified URL will be queued and processed asynchronously.
2. View Results:

The index page will display the results of the submitted jobs, showing the URL and the word count.