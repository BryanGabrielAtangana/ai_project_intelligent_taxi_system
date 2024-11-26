# Intelligent Taxi Simulator

An interactive simulation showcasing intelligent autonomous taxis navigating a grid-based city. The taxis optimize their movements using pathfinding algorithms like A\* to pick up and drop off passengers, manage battery levels, and recharge at stations when needed.

## Features

- **Grid-based environment**: Taxis navigate a city represented by a grid.
- **Pathfinding with A\***: Optimal routes are calculated to reach destinations while avoiding obstacles.
- **Battery management**: Taxis monitor their battery levels, recharge when needed, and avoid running out of power.
- **Control center**: A control center assigns each taxi to a waiting passenger
- **Passenger management**: Taxis pick up and drop off passengers dynamically based on availability.
- **Charging stations**: Strategically placed stations allow taxis to recharge their batteries.
- **Dynamic obstacles**: Taxis adapt their paths in real-time to avoid obstacles.

## Performance Metrics

To evaluate the efficiency of the taxis, the following metrics are measured during the simulation:

1. **Ride Completion Rate**

   - Percentage of successfully completed passenger rides compared to total ride requests.
   - **Formula**:
     ![image](https://github.com/user-attachments/assets/7ca78934-0772-4895-b4eb-3db6ce005cba)

2. **Battery Efficiency**

   - Average battery consumption per completed ride.
   - **Formula**:

   ![image](https://github.com/user-attachments/assets/a514ca0c-4d2a-477d-947f-4f031a41aa6c)

3. **Idle Time**

   - Total time a taxi spends waiting without passengers or tasks.

4. **Average Ride Duration**

   - Time taken to complete a ride from pickup to dropoff.

5. **Charging Efficiency**

   - Time spent recharging compared to operational time.

6. **Distance Traveled**
   - Total distance covered by each taxi during the simulation.

All metrics are displayed on the simulation window.

## Prerequisites

- Python 3.8+
- `pygame` library for visualization

## Installation

1. Clone the repository:

   ```bash
   git@github.com:BryanGabrielAtangana/ai_project_intelligent_taxi_system.git
   cd ai_project_intelligent_taxi_system
   ```

2. Install dependencies:

   ```bash
   pip install pygame
   ```

   or

   For mac O.S

   ```
   pip3 install pygame
   ```

3. Run the simulation:
   ```bash
   python main.py
   ```
   or
   For mac O.S
   ```
   python3 main.py
   ```

## File Structure

- **`main.py`**: Entry point of the simulation.
- **`composants/`**:
  - `taxi.py`: Taxi behavior and management logic.
  - `taxi_stop` : Class contains the points where the rides will be completed.
  - `passenger.py`: Passengers with destination of each.
  - `charging_station.py`: Logic for charging stations.
  - `display_stats`: Class to display the stats.
  - `obstacle`: Obstacle behavior. Can be static or dynamique.
- **`algorithmes.py`**: Pathfinding and related algorithm.

## How it works

1. **Run the Simulation**  
   Launch `main.py` to start the simulation. The grid, taxis, passengers, and charging stations will appear on the screen.

2. **Assign Passengers**  
   Passengers are dynamically assigned to available taxis. The taxi color changes to red when occupied.

3. **Monitor Battery Levels**  
   Each taxi has a battery indicator displayed above it. Green indicates sufficient battery, yellow indicates medium, and red warns of low battery.

4. **Recharge**  
   When a taxi’s battery is low, it automatically heads to the nearest charging station.
