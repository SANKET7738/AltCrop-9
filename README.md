## AltCrop

###INTRODUCTION
KISAN CARE is a web - app that is made to help farmers and government officials related to agriculture. This app uses a machine learning algorithm that takes the location of the farmer as an input and generates an output of crop names that are suitable for the area. The recommendations are made by taking into account various parameters like rainfall, water availability, season-wise crop production in all indian states. India is an agricultural country. Despite the fact that agriculture accounts for as much as a quarter of the Indian economy and employs an estimated 60 percent of the labor force, it is considered highly inefficient, wasteful, and incapable of solving the hunger and malnutrition problems. Despite progress in this area, these problems have continued to frustrate India for decades. It is estimated that as much as one-fifth of the total agricultural output is lost due to inefficiencies in harvesting, transport, and storage of government-subsidized crops.
In KISAN CARE, we aim to help the farmers by using modern computational technique of machine learning to give them intelligent analysis of their farm locations using insights from huge amount of data collected by the Indian Government. Farmers have to give their location in the form of State name and District name. The app then uses these as input parameters for an algorithm that recommends a list of crops that will be beneficial for the region.

### DATA COLLECTION
Data was collected from various datasets provided by the Government of India. Multiple datasets containing portions of relevant data were collected and then processed and integrated into a single master-dataset using dataframe tools. Three different datastes viz. District wise crop details, District wise rainfall, District wise water availabitlity were collected. The data was cleaned, labelled and only needed data was integrated into one dataset.

### ML MODEL
The above dataset was fed to a machine learning algorithm called the Decision Tree Classifier. This algorithm uses the input district and state and makes a recommendation of list of crops that might lead to a better yield for the farmers. Decision tree is a supervised learning model used by experts for predictions by analyzing data.
