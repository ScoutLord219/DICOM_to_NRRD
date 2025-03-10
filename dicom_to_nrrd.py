import os
import sys

volume_nodes = slicer.util.getNodesByClass('vtkMRMLScalarVolumeNode')
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
nrrd_file_name = input("Please provide a name for the anonymized file: ")

if len(volume_nodes) == 0:
    raise ValueError("ERROR: No volume nodes within the scene")

v_node = volume_nodes[0]

new_file_path = os.path.join(desktop_path, nrrd_file_name + '.nrrd')

if v_node:
    slicer.util.saveNode(v_node, new_file_path, {'fileType': '.nrrd'})
    print(f"DICOM data saved as NRRD as: {nrrd_file_name}")
else:
    print("Failed to load DICOM data.")

slicer.mrmlScene.Clear(0)
print("Cleared scene of all nodes")

nrrd_node = slicer.util.loadVolume(new_file_path)

if nrrd_node:
    print(f"Loaded volume {nrrd_file_name}")
else:
    print(f"Failed to load {nrrd_file_name} into scene")
