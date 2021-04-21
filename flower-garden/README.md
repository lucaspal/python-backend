# Tom's Flower Garden

Tom is a scientist who makes experiments on plants. For his current experiment he has decided to grow an outside garden of flowers and observe its behaviour under an environment with controlled weather.
Each day, Tom sets up the weather into the environment, from one of the following: Sunny, Cloudy and Rain.
The flowers Tom cultivates are also very specific. He cultivates 3 types of flowers: Red, Yellow and Blue. Regardless of the color, each flower has two characteristics of interest: Height (in cms) and Hydration (%). Let's take a look at the profile of each flower:
 
1. Red
Temperate flower. Starts with a height of 4-6cm and hydration of 30-60%.
During Rainy days it gains 10% hydration, during Cloudy days it loses 2% hydration, during Sunny days it loses 5%.
Every sunny day it grows 1cm. If its hydration is below 20% or above 85% it loses half a cm instead (regardless of the type of day).
Can't grow more than 10cm.
Dies if its height is less than 2.5cm.
 
2. Yellow
Arid flower. Starts with a height of 6-9cm and hydration of 20-35%.
During Rainy days it gains 20% hydration, during Cloudy and Sunny days loses 5%.
As long as its hydration is greater than 10% but no greater than 40%, it gains 1.5cm per day. Otherwise it loses 1cm.
Can't grow more than 20cm.
Dies if its height is less than 4cm.

3. Blue
Arctic Flower. Starts with a height of 6-7.5 cm and hydration of 40-70%.
During Rainy days it gains 10% hydration. During Cloudy days its hydration remains unchanged. During sunny days it loses 5%.
Can't grow more than 12cm.
Loses 1cm during sunny days, gains 0.5cm during Rainy days. During Cloudy days, gains 0.5cm but only if its hydration is greater than 35%.
Instantly dies if its height is less than 1cm or its hydration falls below 15%.
 
Note: During a day it is first the hydration of a flower that changes. After that effects on the height are evaluated.
 
Write a program that can simulate Tom's Experiment for a (random) garden of flowers and (random) weather conditions.
- You can have as many flowers as you want.
- You can choose to input the data from a file, from console, or generate it randomly.
- Setup a number of iterations (days), say 100, but stop if all flowers are dead.
- Print the state at the end of each day.
 
 

