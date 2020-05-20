# Plant_Leaf_Disease_Classification
### Objective
 Agriculture is one of the main factors that decide the growth of any country. In India it around 65% of the population is based on agriculture. Due to various seasonal conditions the crops get infected by various kinds of diseases. These diseases firstly affect the leaves of the plant and later infected the whole plant which in turn affect the quality and quantity of crop cultivated. <br>
 Hence, we decided to introduce the artificial intelligence based automatic plant leaf disease detection and classification for quick and easy detection of disease and then classifying it.
<br>This approach of ours goals towards increasing the productivity of crops in agriculture. In this approach we have followed several steps i.e. image dataset collection (total of around 52,000 images), image preprocessing consists of various subsets like removing noise, converting image to hsv color space, segmentation using k-means, classification using best performing algorithm and finally developing GUI. 

### Published Research Paper
We have successfully published our paper titled **Classification of Plant Leaf Diseases Using Machine Learning and Image Pre Processing Techniques** in Confluence 2020 under IEEE.
* You can find our paper at:- **https://ieeexplore.ieee.org/document/9057889**



#### Dataset
The dataset is too large to be uploaded and we have used the datset from https://github.com/spMohanty/PlantVillage-Dataset 

#### Libraries Required
* numpy
* pandas
* matplotlib
* keras
* scikit learn
* openCV
* Pyqt5
#### IDE Used
* Pycharm
* Jupyter Notebook

#### Methodology
![image](https://user-images.githubusercontent.com/46081301/82466381-f78ec400-9add-11ea-8ef8-b84b93d534aa.png)
##### Dataset Collection
Training data for machine learning (ML) is an important input of algorithms that remember information to understand such data and predict the future. However, during the development of the ML there are various factors that cannot be accomplished without various important tasks.
![image](https://user-images.githubusercontent.com/46081301/82466573-37ee4200-9ade-11ea-990e-a6d7e249176f.png)

##### Image Preprocessing
* Images are resized to smaller pixel size in order to speed up the computations. 
* The noise is removed using some filtering techniques like Gaussian Blur.
* RGB format is unable to separate image intensity.
* Hence, converted to another color space that is HSV which separate color from intensity.
![Capture](https://user-images.githubusercontent.com/46081301/82466837-80a5fb00-9ade-11ea-9e3d-e788d57e0c53.JPG)

##### Segmentation
* Segmentation is performed using K-means clustering with 2 cluster centers 
* After finding the two clusters ,one with background and other one with leaf part, the clustered image is used to change the pixel     value of the background of the leaf to black.
* By doing so the useless information  from the image is eliminated which in turn increases accuracy.
![Capture](https://user-images.githubusercontent.com/46081301/82467531-615b9d80-9adf-11ea-8731-5da687785213.JPG)

##### Selection of Classifier 
Selected four classifiers namely – 
* 1. Logistic Regression
* 2. KNN
* 3. SVM 
* 4.  CNN
![Capture](https://user-images.githubusercontent.com/46081301/82467241-15a8f400-9adf-11ea-8851-211f9754d1e0.JPG)
##### Refinement of CNN Model
* The dataset has been increased to 52,000 images in order to capture more plant leaf diseases.
* Due to increment of dataset there are now 38 total classes to classify.
* The CNN model has to be good enough to capture all complex patterns.The Convolutional Layers increased to 6,units in last Dense layers are now 38
##### GUI Development
* We have used Qt designer tool to firstly design the basic structure of GUI then we merge our functions to the respective buttons.
* Command used to convert ui to py file - 	C:\Python36\Scripts\pyuic5.exe -o FirstApp.ui FirstApp.py
###### Screenshots of GUI
Shows the home screen of GUI which contains all the push buttons like Choose Image, Preprocess Image and Prediction
![Capture](https://user-images.githubusercontent.com/46081301/82467930-dfb83f80-9adf-11ea-9456-12cc991709d9.JPG)

When clecked on preprocessing button 
![Capture](https://user-images.githubusercontent.com/46081301/82468021-f6f72d00-9adf-11ea-9a21-d83dc90bea14.JPG)

The predicted disease
![Capture](https://user-images.githubusercontent.com/46081301/82468080-09716680-9ae0-11ea-9f39-721389f8b7b8.JPG)

##### Future Work
* The following model can be extended by using even more large dataset with more categories of diseases and the accuracy can also be improved by tuning the hyperparameters.
* The remedies for the classified diseases can also be included in the model. 
* The model then can be deployed on android and as well as iOS platform to reach out the farmers who can make the actual use of the proposed system.



