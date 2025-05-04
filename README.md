# F1 Telemetry Visualization

This repository provides tools for analyzing and visualizing Formula 1 telemetry data using Python. It leverages open-source data to generate insightful plots and comparisons from race sessions.

The setup includes Docker support for consistent execution across environments.

## Features

- Access to historical F1 telemetry data
- Visualization of car performance metrics
- Dockerized environment for easy deployment

## Getting Started

To run the project using Docker:

```bash
docker build -t f1-telemetry .
docker run --rm -v $(pwd):/app f1-telemetry
````

Output plots and files will be saved to the local project directory.

## Requirements

* Docker
* Internet connection (for initial telemetry data fetch)
