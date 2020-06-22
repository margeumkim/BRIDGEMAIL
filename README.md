# BRIDGEMAIL

## Purpose: 
This project aims to help email communications between new teammates who are sitting far apart in a company's email network. The idea is that by analyzing the archive of past emails within a company, one can inform a user of the likelihood of language discrepancies with a new teammate, and provide insights into what those discrepancies would look like. The final product have three functions -- stranger detector, jargon detector, and context detector. Currently, these three fucntions are developed for senders--that is, they help users tune their language when they are composing messages. 

* Stranger Detector: Stranger detector provides a sender with a score, which shows the distance between the sender and the recipient in the email network. As a metric for the distance, I chose Shortest path length, which indicates how many steps the sender must go in the email network to reach the recipient. 

* Jargon Detector: Jargon detector tells a sender that s/he is using words that are jargon to the recipient. I define jargon as words that the recipient never used/encountered in his/her email account. I use bag of words appraoch to list non-overlapping words for each of distant pairs, defined as users who are three or more steps away from each other (shortest path length >= 3).

* Context Detector: Context detector provides a sense of what a certain word might mean in the recipient. The idea is that the same word might be associated with different meanings in differen users' email contexts. Therefore, I use BERT, a word-embedding model, to extract what certain words mean in each user's context. To get at the contextualized meaning, I look at BERT's attention matrix and extract top 20 words that received most attention from a word of interest. I provide these top 20 words to the user if s/he uses the word in the content of a email. 


## Data: 
* Enron email dataset: https://www.kaggle.com/wcukierski/enron-email-dataset/data#
* Labeled dataset: https://data.world/brianray/enron-email-dataset

## Code:

* 00_parse_email: 
  * What it does: Parse the email data into separate columns and store for later use 
  * Input: Enron dataset (emails.csv)
  * Output: Parsed email dataframe (emails_parsed.csv)

* 01_network_analysis
  * What it does: Create an edgelist, import into a graph, perform network EDA, and calcualte and store pairwise shortest path length information  
  * Input: Enron dataset (emails_parsed.csv)
  * Output: path length data (***==XXXXXXX==.csv***), distant pair list (***==XXXXXXX==.csv***)

* 02_bag_of_words
  * What it does: Create bag of words for each user, for each of the distant pairs, create and store a list of non-overlapping words
  * Input: Enron dataset (emails_parsed.csv)
  * Output: Parsed email dataframe (***==XXXXXXX==.csv***)

* 03_tfidf
  * What it does: Create a dictionary of words that are used frequenctly across all users and all email topic categories (words in this dictionary are presumably used in  multiple context by many users) 
  * Input: Enron dataset (emails_parsed.csv), label information (***==XXXXXXX==.csv***)
  * Output: Dictionary of context-dependent words (**dict_for_bert.csv**)

* 04_bert_train
  * What it does: 
  * Input: Enron dataset (emails.csv), label information (***==XXXXXXX==.csv***),  Dictionary of context-dependent words (**dict_for_bert.csv**)
  * Output: Fine-tuned models (***==XXXXXXX==.YYY***), Fine-tuned models (***==XXXXXXX==.YYY***), Fine-tuned models (***==XXXXXXX==.YYY***)

* 05_bert_evaluate
  * What it does:  
  * Input: Enron dataset (emails.csv), Fine-tuned models (***==XXXXXXX==.YYY***), Fine-tuned models (***==XXXXXXX==.YYY***), Fine-tuned models (***==XXXXXXX==.YYY***)
  * Output: User-level word-sense information ((***==XXXXXXX==.YYY***)

* 06_web_app
  * What it does: 
  * Input: path length data (***==XXXXXXX==.csv***),  Dictionary of context-dependent words (**dict_for_bert.csv**), User-level word-sense information ((***==XXXXXXX==.YYY***)
  * Output: 


