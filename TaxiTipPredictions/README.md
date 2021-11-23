# Predicting Taxi Tips in NYC

As a European ride-sharing services company aiming to launch our product in the USA, we have chosen New York as our starting point. One of the upgrades we would like to build on our existing app to enter this market is a feature able to advise our customers on how much they should tip according to the characteristics of their trip. Our objectives are:

* Optimise our app by creating a system to advise our customers on how much they should tip.
* Provide our drivers with information on how to obtain the best tips.

Since we have no previous experience in the city, we do not know its customers' behaviour. Moreover, we do not have historical data of our own to make tip predictions. As a solution, I have taken a dataset with 6 million yellow cab trips (August 2019) from the <a href="https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page">NYC Open Portal.</a></li> I will use this information as a first approach to generate insights about mobility in the city and to build a model able to recommend tip quantities to customers.

![Taxi](./resources/taxi.jpg "Taxi")

<h2></h2>
This project is divided into two notebooks:
<br></br>
<ol>
  <li>Data preparation, exploration and model development.</li>
  <li>Quick demo to test the model. Please check the <a href="https://share.streamlit.io/mbescansa/predicting-taxi-tips-in-nyc/main/app_taxi_tip_predictor.py">web application</a> I developed with it.</li>
</ol> 
</body>
</html>
Additionally you can find an interactive <a href="https://public.tableau.com/app/profile/marta4014/viz/NYC-Taxitippingbehaviour/Dashboard1">Tableau dashboard</a> that you can navigate to learn some more insights about the data.
<br></br>


# Conclusions
The resulting model has a limited accuracy rate of 65% that might be improved by adding further data spread across a wider timeline. Still, problems of subjective nature such as tipping or liking a certain product can only be predicted to a certain extent because there is no universal consensus about it.

Nevertheless, the exploratory analysis has uncovered some insights that can be beneficial for our business. In more affluent parts of the city and during peak hours, a higher percentage tip will be paid to any taxi driver. Given the fact that there is a good relationship between distance, duration and tip amount, we could use this information to identify bonus areas and create a reward system for our best drivers by allocating them in those areas more often.
