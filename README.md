
# Parms-Extraction_Galaxy_Merger_DL

To Find Dynamical Parameters of Galaxy 

## Step 1: Download Images in Bulk

Use Download.py for downloading images and settings.ini file for configuration 
For settings:
1. Open settings.ini in any editor
2. In angles put the range of &Theta; and &Phi;
3. Insert with what step the angle should increase
4. put the other parameters 
5. Run the GalMer query at http://galmer.obspm.fr/
6. For selecting checkboxes present on the visualization page after querying on GalMer ; put 1 if checked and 0 if unchecked
7. Select the Run you want to download
8. Find the show number for the timestamp you want to select as shown in the Image 
![image](https://user-images.githubusercontent.com/67388655/129602029-c49a6962-336b-4e66-a930-68f4afae4cda.png)
9. Insert the show number in the settings.ini experiments/shows:
10. Go to line number 61 in Download.py and update the spin for which you have ran the query (As shown in the figure)

![image](https://user-images.githubusercontent.com/67388655/129600188-e09f1165-c7cf-4172-998f-e821561f7023.png)

For example:
![image](https://user-images.githubusercontent.com/67388655/129599891-eef34816-4b46-4077-93b2-c97914388f1c.png)

NOTE: Downloading of the Images might be slower than your Internet speed

## Step 2: Clone or Download the repository
Use 
```git clone https://github.com/JanvitaReddy/Parameters-determination.git```
Or Download and extract the Repository


## Step 3: Installation of Libraries 
Installation of Autokeras
Can Refer to https://github.com/keras-team/autokeras
or can simply use 
```python
pip install git+https://github.com/keras-team/keras-tuner.git
pip install autokeras
```

## Step 4: Running the Deep Learning Model
### Case 1: 
For using Pretrained Model or for gSa and gSb interaction: 

Run Detect.py for corresponding Images 

Note here:
1. Model is trained for Image of dimensions 64x64x3. To run the model please resize the image to the 64x64x3 dimensions
2. The folder "model" in cloned repository should be 94.8 MB (9,94,96,042 bytes). If it dosen't match, it is advised to download from https://bit.ly/3jU0ir7

### Case 2:
For training the new model for different data:
1. Optional- You can clone the repository or download the model from the link https://bit.ly/3jU0ir7
2. Use the pretrained weights or you can train the model from scratch from https://autokeras.com/
3. Can use the Detect.py for corresponding Images supplying path of newly trained model



