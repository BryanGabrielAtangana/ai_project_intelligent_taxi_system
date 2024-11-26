# Intelligent Taxi Simulator  

An interactive simulation showcasing intelligent autonomous taxis navigating a grid-based city. The taxis optimize their movements using pathfinding algorithms like A* to pick up and drop off passengers, manage battery levels, and recharge at stations when needed.  

## Features  
- **Grid-based environment**: Taxis navigate a city represented by a grid.  
- **Pathfinding with A***: Optimal routes are calculated to reach destinations while avoiding obstacles.  
- **Battery management**: Taxis monitor their battery levels, recharge when needed, and avoid running out of power.
- **Control center**: A control center assigns each taxi to a waiting passenger 
- **Passenger management**: Taxis pick up and drop off passengers dynamically based on availability.  
- **Charging Stations**: Strategically placed stations allow taxis to recharge their batteries.  
- **Dynamic Obstacles**: Taxis adapt their paths in real-time to avoid obstacles.  

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

4. Run the simulation:  
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
  - `passenger.py`: Passengers with destination of each.  
  - `charging_station.py`: Logic for charging stations.
  - `display_stats`: Class to display the stats.
  - `obstacle`: Obstacle behavior. Can be static or dynamique.
- **`algorithmes/`**: Pathfinding and related algorithm.  

## How to Use  

1. **Run the Simulation**  
   Launch `main.py` to start the simulation. The grid, taxis, passengers, and charging stations will appear on the screen.  

2. **Assign Passengers**  
   Passengers are dynamically assigned to available taxis. The taxi color changes to red when occupied.  

3. **Monitor Battery Levels**  
   Each taxi has a battery indicator displayed above it. Green indicates sufficient battery, yellow indicates medium, and red warns of low battery.  

4. **Recharge**  
   When a taxi’s battery is low, it automatically heads to the nearest charging station.  
