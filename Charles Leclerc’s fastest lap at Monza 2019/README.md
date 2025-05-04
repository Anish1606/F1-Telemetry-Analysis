# F1 Telemetry Analysis - Leclerc Fastest Lap at Monza 2019

This project uses the **FastF1** Python library to retrieve and visualize telemetry data from the **2019 Formula 1 Italian Grand Prix** (Monza). The analysis focuses on **Charles Leclerc’s fastest lap** during the race, plotting his car’s speed over time.

The project is designed to run inside a **Docker** container, making it easy to deploy and share with others.

---

## Features

- Loads session data for Monza 2019 and picks Leclerc’s fastest lap.
- Visualizes the speed vs. time for Leclerc’s fastest lap using **Matplotlib**.
- Dockerized environment for easy setup and execution.

---

## Requirements

The project requires the following Python libraries:

- **FastF1**: Library for accessing F1 telemetry data.
- **Matplotlib**: For plotting the telemetry data.
- **Pandas**: For data handling.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Anish1606/f1-telemetry-analysis.git
cd f1-telemetry-analysis
```

### 2. Build Docker Image

```bash
docker build -t f1-leclerc .
```

### 3. Run the Docker Container

```bash
docker run --rm -v ${PWD}:/app f1-leclerc
```

The script will fetch the telemetry data, process it, and generate a plot showing Leclerc’s fastest lap speed. The plot will be saved as `leclerc_plot.png` in the current directory.

---

## Plot Output

The script generates a plot of **Charles Leclerc's fastest lap speed** at Monza 2019 and saves it as `leclerc_plot.png`. The plot shows:

* **X-axis**: Time (in seconds)
* **Y-axis**: Speed (in km/h)

---

## Resources

* [FastF1 Documentation](https://docs.fastf1.dev/) – Official guide for using the FastF1 Python library to access and analyze Formula 1 telemetry data.

---
