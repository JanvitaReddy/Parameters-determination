
# Parms-Extraction_Galaxy_Merger_DL

To Find Dynamical Parameters of Galaxy 

## Step 1: Download Images in Bulk

![Alt test](https://drive.google.com/file/d/14INH2vADWHrdueTYehaS2gbRj70aPT4F/view?usp=sharing)
![sideview](https://user-images.githubusercontent.com/67388655/129599651-44600d8f-1d4c-4528-ba2c-85fee31026b7.png)

## Step 2: Clone or Download the repository
Use 
```git clone https://github.com/adarsh3601/Parms-Extraction_Galaxy_Merger_DL.git```



## Step 3: Installation of Libraries 
Installation of Autokeras
Can Refer to https://github.com/keras-team/autokeras
or can simply use 
```python
pip install git+https://github.com/keras-team/keras-tuner.git
pip install autokeras
```
For python3
```python
python3 -m pip install git+https://github.com/keras-team/keras-tuner.git
python3 -m pip install autokeras
```
Installation of Tensorflow
```python
pip install tensorflow
```
## Step 4: Running the Deep Learning Model
### Case 1: 
For using Pretrained Model or for gSa and gSb interaction: 

Run Detect.py for corresponding Images 

Note here:
1. Model is trained for Image of dimensions 64x64x3. To run model flawlessly please resize the image to the 64x64x3 dimensions
2. The folder "model" in cloned repository should be 94.8 MB (9,94,96,042 bytes). If it dosen't match, it is advised to download from https://bit.ly/3jU0ir7

### Case 2:
For training the new model for different data:
1. Optional- You can clone the repository or download the model from the link https://bit.ly/3jU0ir7
2. Use the pretrained weights or you can train the model from scratch from https://autokeras.com/
3. Can use the Detect.py for corresponding Images supplying path of newly trained model



