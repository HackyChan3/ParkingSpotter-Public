from roboflow import Roboflow
import os
from secrets import RF_API_KEY, RF_WORKSPACE, RF_PROJECT, RF_VERSION, INPUT_DIR, OUTPUT_DIR

rf = Roboflow(api_key=RF_API_KEY)
project = rf.workspace(RF_WORKSPACE).project(RF_PROJECT)
print(project.versions)

model = project.version(RF_VERSION).model

# Directory containing the parking lot images
input_dir = INPUT_DIR
output_dir = OUTPUT_DIR

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all 10 parking images
for i in range(1, 11):
    # Construct the input file path
    input_path = os.path.join(input_dir, f"apl_test_{i}.png")
    
    # Check if file exists
    if os.path.exists(input_path):
        print(f"\nProcessing image {i}/10: {input_path}")
        
        # Run inference
        result = model.predict(input_path, confidence=40)
        
        # Save output with unique name
        output_path = os.path.join(output_dir, f"apl_test_output_{i}.jpg")
        result.save(output_path)
        
        # Print detection count
        num_detections = len(result.json()['predictions'])
        print(f"Detected {num_detections} cars in image {i}")
    else:
        print(f"Warning: {input_path} not found, skipping...")

print("\nAll images processed!")