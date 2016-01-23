# Word Cloud Generator

Takes a twitter user's username, creates a wordcloud, and saves image to username.png. Requires  [wordcloud](https://github.com/amueller/word_cloud), [matplotlib](http://matplotlib.org/users/installing.html) and SciPy.
To run, run the following script:
```
$ ./makeWordCloud.sh  twitter-username
```
To change colors, change the numbers in makeWordCloud.py in the function *my_color_func*   
Hue values are between 0 and 360, follow rainbow: 
```
  Red Orange Yellow Green Blue Indigo Violet
   0   50  100  150  200  250  300   360
```
# Examples
Neil deGrasse Tyson
![neil tyson](https://github.com/araval/Twitter-Word-Cloud-Generator/blob/master/images/neiltyson.png)

Naomi Klein (author of The Shock Doctrine)
![naomi klein](https://github.com/araval/Twitter-Word-Cloud-Generator/blob/master/images/naomiaklein.png)

Joyce Carol Oates
![hc](https://github.com/araval/Twitter-Word-Cloud-Generator/blob/master/images/joycecaroloates.png)

Rihanna
![rihanna](https://github.com/araval/Twitter-Word-Cloud-Generator/blob/master/images/rihanna.png)

Hillary Clinton
![hc](https://github.com/araval/Twitter-Word-Cloud-Generator/blob/master/images/hillaryclinton.png)

Donald Trump
![trump](https://github.com/araval/Twitter-Word-Cloud-Generator/blob/master/images/realdonaldtrump.png)

Bernie Sanders
![berniesanders](https://github.com/araval/Twitter-Word-Cloud-Generator/blob/master/images/berniesanders.png)
