from flask import Flask, request, jsonify, render_template
import time
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def linear_search(text, query):
    matches = []
    for i in range(len(text) - len(query) + 1):
        if text[i:i+len(query)].lower() == query.lower():
            matches.append(text[i:i+len(query)])
    return matches

def binary_search(words, query):
    words.sort()  # Pre-sort for binary search
    left, right = 0, len(words) - 1
    matches = []
    while left <= right:
        mid = (left + right) // 2
        if words[mid].lower() == query.lower():
            matches.append(words[mid])
            return matches  # Return first match for simplicity
        elif words[mid].lower() < query.lower():
            left = mid + 1
        else:
            right = mid - 1
    return matches

def naive_string_matching(text, query):
    matches = []
    n, m = len(text), len(query)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j].lower() == query[j].lower():
            j += 1
        if j == m:
            matches.append(text[i:i+m])
    return matches

def compute_lps(query):
    m = len(query)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if query[i] == query[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, query):
    matches = []
    n, m = len(text), len(query)
    lps = compute_lps(query)
    i = j = 0
    while i < n:
        if query[j].lower() == text[i].lower():
            i += 1
            j += 1
        if j == m:
            matches.append(text[i-j:i])
            j = lps[j-1]
        elif i < n and query[j].lower() != text[i].lower():
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return matches

def bad_char_heuristic(query):
    bad_char = {}
    for i in range(len(query)):
        bad_char[ord(query[i].lower())] = i
    return bad_char

def boyer_moore_search(text, query):
    matches = []
    n, m = len(text), len(query)
    bad_char = bad_char_heuristic(query)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and query[j].lower() == text[s + j].lower():
            j -= 1
        if j < 0:
            matches.append(text[s:s+m])
            s += m - bad_char.get(ord(text[s + m].lower()) if s + m < n else 0, -1)
        else:
            s += max(1, j - bad_char.get(ord(text[s + j].lower()), -1))
    return matches

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    file = request.files['file']
    algorithm = request.form['algorithm']
    query = request.form['query']

    if not file or not query:
        return jsonify({'error': 'Missing file or query'}), 400

    # Save and read file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Measure execution time
    start_time = time.time()
    if algorithm == 'linear':
        matches = linear_search(text, query)
    elif algorithm == 'binary':
        words = text.split()
        matches = binary_search(words, query)
    elif algorithm == 'naive':
        matches = naive_string_matching(text, query)
    elif algorithm == 'kmp':
        matches = kmp_search(text, query)
    elif algorithm == 'boyer_moore':
        matches = boyer_moore_search(text, query)
    else:
        return jsonify({'error': 'Invalid algorithm'}), 400
    end_time = time.time()

    execution_time = end_time - start_time
    return jsonify({
        'matches': matches,
        'time': execution_time
    })

if __name__ == '__main__':
    app.run(debug=True)