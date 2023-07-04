# SII
Here we create an app that loads the data and shows an analysis of the National Greenhouse and Energy Register for 2021-22 reporting year using the publicly available data.

## Description
We will be using the 'Greenhouse and energy information by registered corporation 2021-22' data from the The Clean Energy Regulator website. The data has 417 observations and the dataset includes the organisation name, identifying details (ABN), Total scope 1 emissions (t CO2-e), Total scope 2 emissions (t CO2-e), Net energy consumed (GJ) and important notes. 

## Purpose of the app
We will load the data to a dataframe and make a histogram of the Net energy consumed (GJ) feature. And further find the average of the total scope 1, 2 emissions and net energy consumed.

## Installation and Uses
The callback has an Input and an Output, which are properties of specific components. In this example, the callback:

- takes as input the value property of component with id='dropdown' which is the item we selected from the dropdown
- gives as output the figure property with id=’histogram’, which is the histogram of the feature value

The properties must be passed as strings in the Input, Output properties (here ‘value’ and ‘figure’ instead of value and figure). The variable we used in the update_hist function (which we named feature) takes the value of the input value. Callbacks can have multiple inputs and outputs.

## Expecations 
