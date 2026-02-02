# Main code to detect objects using Roboflow model.
#
# Note to viewer: this is unnecessary 
# if you are using the Streamlit app (st_site.py).

from roboflow import Roboflow
from configs import RF_API_KEY, RF_WORKSPACE, RF_PROJECT, RF_VERSION

rf = Roboflow(api_key=RF_API_KEY)
project = rf.workspace(RF_WORKSPACE).project(RF_PROJECT)
print(project.versions)

model = project.version(RF_VERSION).model  # Use 1, 2, 3, etc. based on your version

# Run inference
result = model.predict("C:\\Users\\shilp\\.AbhijeetProjectFiles\\Parking Lot Detector\\images\\val\\parking_image_val2.png", confidence=40)
result.save("output.jpg")
