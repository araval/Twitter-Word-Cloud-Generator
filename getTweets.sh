username=$1
curl "http://greptweet.com/create.php?id=$username"

url="http://greptweet.com/u/$username/tweets.txt"
wget $url

mv tweets.txt tweets.txt.gz
gunzip tweets.txt.gz
awk -F '|' '{print $3}' tweets.txt > tmp
mv tmp tweets.txt
python makeWordCloud.py
#mv tweets.txt $username".txt"
rm tweets.txt
mv tmp.png $username.png
