from flask import Flask, render_template, request
import pickle, numpy as np

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))

app = Flask(__name__)
#    publish_year = list(popular_df['Year-Of-Publication'].values),

@app.route('/')
def index():
    return render_template('index.html',                 
                           book_name = list(popular_df['Book-Title'].values),
                           author = list(popular_df['Book-Author'].values),
                           votes = list(popular_df['Num-Rating'].values),
                           ratings = list(popular_df['Avg-Num-Rating'].values),
                           image_url = list(popular_df['Image-URL-S'].values),
                           )
@app.route('/recommend')
def recommend_page():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index==f"{user_input}")[0][0]
    similar_items_index = sorted(list(enumerate(similarity_score[index])), key = lambda x : x[1],reverse=True)[1:5]
    data = []
    for book_index in similar_items_index:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[book_index[0]]] #Getting similar book name using index
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    return render_template('recommend.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)