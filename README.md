# Spam_Email_Detection

In this task i create a spam email  detector using python and machine learning. And create a web app for detection using
streamlit framework.For dataset i download it from kaggle.com . I used jupyter notebook for data cleaning to model building.

## Dataset
This dataset contain 5572 row and 2 column. The column in the dataset as given below:

1.Category

2.Message


## 🛠 Technologies Used

    * Language: Python
    * IDE : Jupyter Notebook ,Visual studio
    * Analytical tools : (pandas,statstical method ,NUmpy) for
              data cleaning && (Matplotlib and seaborn )for EDA
    * Model BUilding : sklearn
    * Framework : Streamlit


## Data Cleaning

In the data cleaning section , first i check foe null value.Thank to kaggle there is no any missing value. I used label encoder to convert category feature  string valueinto
numeric value where i label spam as a 1 and ham as  0. Then i check and remove all duplicate messages. 

## EDA

In this section, i used count_value() function to how many message are ham and spam after duplication remove. Ater that i build a piechart to see number of message in pictorial form.
I install and import nltk which help us to find how many charater , words and sentences used in message. i download puntk and stopwords . I create a new column by using apply len in 
message which give length in term of charater usesof every message.  likewise , i crete another two column  that give number of sentence of each message and number of words of each
message. And then, plot histgram to see realtionship between spam and ham message .Create a pairplot to show relation between characters ,words ,sentences.

## Data preprocessing

In this section, first i convert message in lowercase,tokenize that message , remove a special characters , remove stopwords and punctuation and them create  new column for converted message.
I generate a word cloud for spam and ham message.

## Model BUilding
First,I convert the message into number using vectorization. Then , I train and test dataset . I used three model of  naivebayes  then according to accuray_score and precision_score
bernoulli model give highest accuracy and precision score i.e 97% . So we used bernoulli model for prediction . 


I create vectorize and pickel model and used streamlit framework for deployment.




 





    

