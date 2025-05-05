import random
import time

class Spacecraft:
    def __init__(self, name):
        self.name = name
        self.data_storage = []

    def collect_data(self):
        # Simulate data collection from various instruments
        optical_data = self.collect_optical_data()
        lidar_data = self.collect_lidar_data()
        radar_data = self.collect_radar_data()
        infrared_data = self.collect_infrared_data()
        gravitational_data = self.collect_gravitational_data()
        
        # Store collected data
        collected_data = [optical_data, lidar_data, radar_data, infrared_data, gravitational_data]
        self.data_storage.append(collected_data)
        print(f"Data collected and stored in {self.name}'s data storage.")

        # Classify object based on collected data
        object_type = self.classify_object(collected_data)
        print(f"Identified object: {object_type}")
        print(f"The object identified is a {object_type}.\n")

    def collect_optical_data(self):
        # Simulate optical data collection
        optical_data = {
            'type': 'optical',
            'image': f'Image_{random.randint(1, 100)}',
            'brightness': random.uniform(0.1, 1.0),
            'timestamp': time.time()
        }
        print("Optical data collected.")
        return optical_data

    def collect_lidar_data(self):
        # Simulate lidar data collection
        lidar_data = {
            'type': 'lidar',
            'distance': random.uniform(0.1, 10.0),
            '3d_map': f'3D_Map_{random.randint(1, 100)}',
            'timestamp': time.time()
        }
        print("Lidar data collected.")
        return lidar_data

    def collect_radar_data(self):
        # Simulate radar data collection
        radar_data = {
            'type': 'radar',
            'surface_image': f'Surface_Image_{random.randint(1, 100)}',
            'subsurface_image': f'Subsurface_Image_{random.randint(1, 100)}',
            'timestamp': time.time()
        }
        print("Radar data collected.")
        return radar_data

    def collect_infrared_data(self):
        # Simulate infrared data collection
        infrared_data = {
            'type': 'infrared',
            'thermal_map': f'Thermal_Map_{random.randint(1, 100)}',
            'temperature': random.uniform(100, 300),
            'timestamp': time.time()
        }
        print("Infrared data collected.")
        return infrared_data

    def collect_gravitational_data(self):
        # Simulate gravitational data collection
        gravitational_data = {
            'type': 'gravitational',
            'gravity_field': random.uniform(0.1, 9.8),
            'density': random.uniform(2, 5),
            'timestamp': time.time()
        }
        print("Gravitational data collected.")
        return gravitational_data

    def classify_object(self, collected_data):
        # Example classification logic based on data
        optical_data = collected_data[0]
        lidar_data = collected_data[1]
        radar_data = collected_data[2]
        infrared_data = collected_data[3]
        gravitational_data = collected_data[4]

        # Simple rules for classification (these can be more complex in a real scenario)
        if optical_data['brightness'] > 0.8:
            return 'Satellite'
        elif lidar_data['distance'] < 1.0 and infrared_data['temperature'] > 200:
            return 'Space Debris'
        elif radar_data['surface_image'].startswith('Surface_Image_') and gravitational_data['density'] < 3:
            return 'Asteroid'
        elif gravitational_data['density'] > 4 and infrared_data['temperature'] < 150:
            return 'Comet'
        else:
            return 'Unknown Object'

    def transmit_data(self):
        # Simulate data transmission to Earth
        print(f"Transmitting data to Earth from {self.name}...")
        for data_cycle in self.data_storage:
            for data in data_cycle:
                print(f"Transmitting {data['type']} data: {data}")
        print("Data transmission complete.")
        self.data_storage = []  # Clear storage after transmission

# Main function to run the simulation
def main():
    dimensat = Spacecraft(name="Dimensat")
    detected_objects = set()

    while len(detected_objects) < 4:  # Run until all object types are detected
        dimensat.collect_data()
        object_type = dimensat.classify_object(dimensat.data_storage[-1])
        detected_objects.add(object_type)
        time.sleep(1)  # Simulate time delay between data collection
        dimensat.transmit_data()

    print("All object types have been detected at least once.")

if __name__ == "__main__":
    main()
