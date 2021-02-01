# Text Similarity

This web service checks the text similarity between two texts and gives a metric as a measure for the similarity.
The metric is a numeric value between 0 to 1. When there are no words in common, we will receive a value of 0. If it is an exactly same document, the value received will be 1.

I am using Postman to send a POST request to the web service. The POST request will contain two texts in the body of the payload and the response will be the similarity between the two texts.

The decisions taken to achieve the desired results:
 1. The similarity based metric used is Cosine Similarity. 
 2. Only the words were taken into consideration. Punctuations were removed.
 3. Stop-words and contractions were not considered in the similarity comparison.
 4. The data structures used are sets and dictionaries.
 5. The ordering of words was not considered.

## Running The Application

 - Install the Python packages required to run the application using 
 `$ python -m pip install -r requirements.txt -U`
 
 - Run the application using the following command
 `$ python textSimilarity.py`

## Rest API Endpoints
The POST request is sent to the following endpoint
`http://localhost:8000`

The payload is sent in the body of the POST request. The following is a sample of a body of POST request
```
{
	"text1" : "This is the first text sample." 
	"text2" : "This is the second text sample."
}
```
The response of the POST request is the cosine similarity between text1 and text2.