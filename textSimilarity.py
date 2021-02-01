from flask import Flask, request, jsonify


app = Flask(__name__)


def preprocessing(text1, text2):
    stopwords = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", 
                 "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 
                 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 
                 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 
                 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 
                 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 
                 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 
                 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 
                 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 
                 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 
                 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 
                 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 
                 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', 
                 "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', 
                 "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 
                 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', 
                 "wouldn't"}
    
    frequency1 = {}
    frequency2 = {}
    
    for word in text1.lower().split():
        word = "".join([ch for ch in word if ch.isalnum()])
        if word in stopwords: 
            continue
        if word in frequency1:
            frequency1[word] += 1
        else:
            frequency1[word] = 1
                

    for word in text2.lower().split():
        word = "".join([ch for ch in word if ch.isalnum()])
        if word in stopwords: 
            continue
        if word in frequency2:
            frequency2[word] += 1
        else:
            frequency2[word] = 1
            
    return frequency1, frequency2
    


def cosine_similarity(frequency1 ,frequency2):
    numerator = 0.0
    deno_1 = 0.0
    deno_2 = 0.0
    
    for key ,val in frequency1.items():
        numerator += val * frequency2.get(key, 0.0)
        deno_1 += (val * val)
        
    for val in frequency2.values():
        deno_2 += (val *val)
        
    return numerator / ((deno_1 * deno_2) ** 0.5)



@app.route('/', methods=['POST'])
def is_pyramid_word():
    data = request.json
    frequency1, frequency2 = preprocessing(data["text1"], data["text2"])
    result = cosine_similarity(frequency1 ,frequency2)
    return jsonify("The similarity between text1 and text2 = " + str(result))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True)