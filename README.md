## Simple Search Application

A web-based tool to search text in .txt files using different algorithms and visualize execution time.
Features

Upload .txt files to search for a query.
Choose from five search algorithms: Linear Search, Binary Search, Naive String Matching, KMP, and Boyer-Moore.
View matching results and execution time.
Visualize execution time with a bar chart using p5.js.

**Project Structure**
```
search-app/
├── static/
│   ├── sketch.js        # p5.js code for execution time bar chart
│   └── style.css        # Basic CSS for styling
├── templates/
│   └── index.html       # Main HTML page with UI
├── app.py               # Flask backend with search algorithms
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

```

**Prerequisites**
```
Python 3.8 or higher
Git
A web browser
```

Run the application:python app.py


Open http://localhost:5000 in your browser.


**Usage**

Upload a .txt file using the "Choose File" button.
Select an algorithm from the dropdown (Linear Search, Binary Search, Naive String Matching, KMP, or Boyer-Moore).
Enter a search query in the text field.
Click "Search" to view matches and execution time.
A bar chart below the results shows the execution time in seconds.

**Notes**

File Support: Only .txt files are supported.
Binary Search: Assumes the text is split into words and sorted alphabetically.
Boyer-Moore: Uses a simplified bad character heuristic for string matching.
Performance: Execution time is measured in seconds and visualized in the bar chart.
Temporary Files: Uploaded files are stored in the uploads/ directory. You may need to manually delete them after use.

**Example**

```
Upload a file named sample.txt containing:  AI is great. AI helps in learning. ai is fun. AI AI AI
Select "Boyer-Moore" from the dropdown.
Enter the query "AI".
Click "Search".
Expected output:  
Matches: AI, AI, ai, AI, AI, AI, ai, AI, AI  
Execution Time: ~0.0020 seconds  
A bar chart showing the execution time.
```
**UI**

![image](Screenshot.png)


**Future Improvements**
```
-Support for additional file formats (e.g., .csv, .json).
-Compare execution times across all algorithms in a single search.
-Clean up uploaded files automatically after each session.
```

License
This project is licensed under the MIT License - see the LICENSE file for details.
