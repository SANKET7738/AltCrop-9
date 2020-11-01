## Kisan Care - AI based Crop Recommendation System

## Description

**Kisan Care** is a web - app that is made to help farmers and government officials related to agriculture. This app uses a **machine learning algorithm** that takes the **location** of the farmer as an input and generates an output of crop names that are suitable for the area. The recommendations are made by taking into account various parameters like *rainfall, water availability, season-wise crop production* in all Indian states and Union Territories.  


In **Kisan Care**, we aim to help the farmers by using modern computational technique of machine learning to give them intelligent analysis of their farm locations using insights from huge amount of data collected by the Indian Government. Farmers have to give their location in the form of State name and District name. The app then uses these as input parameters for an algorithm that recommends a list of crops that will be beneficial for the region.

### Data

Data was collected from various datasets provided by the Government of India. Multiple datasets containing portions of relevant data were collected and then processed and integrated into a single master-dataset using dataframe tools. Three different datastes viz. District wise crop details, District wise rainfall, District wise water availabitlity were collected. The data was cleaned, labelled and only needed data was integrated into one dataset.

Datasets - 

1.[District-wise, season-wise crop production statistics](https://data.gov.in/catalog/district-wise-season-wise-crop-production-statistics?filters%5Bfield_catalog_reference%5D=87631&format=json&offset=0&limit=6&sort%5Bcreated%5D=desc)


2.[Sub Divisional Monthly Rainfall from 1901 to 2017](https://data.gov.in/resources/sub-divisional-monthly-rainfall-1901-2017)

3.[State/UT-wise categorisation of Blocks/Talukas/Mandals regarding Online Grant of NOC for Groundwater Extraction during 2013 (From : Ministry of Water Resources, River Development & Ganga Rejuvenation)](https://data.gov.in/resources/stateut-wise-categorisation-blockstalukasmandals-regarding-online-grant-noc-groundwater)

### Model Preparation

After the Data Integration, Cleaninng , labelling and preprocessing the datasets this data was integrated into a single dataset which was used to train the model. For the selection of the model we decided to go with the **Decision Tree Classifier** algorithm for this problem statement.

## Integrating the Model

The model is integrated with the **Django** framework for back-end. *Bootstrap* for user-interface and *SQLite3* for database. The app consists use of **ipstack API** to get the user-location automatically and  **Mapbox API** for map-interface.

