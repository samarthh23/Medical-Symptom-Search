# Medical-Symptom-Search


A Flask web application that uses information retrieval techniques to search for medical conditions based on symptoms.

## Features

- **Symptom-based search**: Enter symptoms to find possible medical conditions
- **Advanced IR techniques**: Uses BM25F ranking algorithm for relevant results
- **Fuzzy matching**: Handles misspellings and typos in search queries
- **Spelling suggestions**: Offers alternative spellings for query terms
- **Comprehensive database**: Includes 25+ common medical conditions with symptoms, descriptions, and treatments
- **Responsive UI**: Clean, user-friendly interface with Bootstrap

## Getting Started

### Prerequisites

- Python 3.7+
- Flask
- Whoosh

### Installation

1. Clone the repository or download the files

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create the search index:
   ```
   python index_data.py
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000/`

## Project Structure

- `app.py` - Main Flask application with search functionality
- `index_data.py` - Script to create and populate the search index
- `templates/` - HTML templates for the web interface
  - `search.html` - Main search page with results display
  - `about.html` - Information about the application
- `indexdir/` - Directory containing the Whoosh search index (created when running index_data.py)

## Information Retrieval Methods

This application implements several IR techniques:

1. **BM25F Ranking**: A state-of-the-art ranking function that incorporates:
   - Term Frequency (TF)
   - Inverse Document Frequency (IDF)
   - Document Length Normalization
   - Field-specific weighting

2. **Text Processing**:
   - Stemming (reduces words to their root form)
   - Fuzzy matching (for misspellings)
   - Multi-field searching (searches across symptoms and synonyms)

## How It Works

1. The user enters symptoms in the search box
2. The application processes the query using Whoosh's search capabilities
3. The system retrieves and ranks relevant medical conditions
4. Results are displayed with detailed information about each condition
5. Related symptoms and spelling suggestions are shown when applicable

## Disclaimer

This application is for informational purposes only and should not replace professional medical advice. Always consult with a healthcare provider for proper diagnosis and treatment.

## License

This project is open source and available under the MIT License.
