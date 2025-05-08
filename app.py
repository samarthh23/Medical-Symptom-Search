# app.py
from flask import Flask, request, render_template, jsonify
from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser, FuzzyTermPlugin, OrGroup
from whoosh import scoring
from whoosh.scoring import BM25F
from whoosh.analysis import StemmingAnalyzer
import os
import traceback

app = Flask(__name__)

# Check if index directory exists, if not create a message
if not os.path.exists("indexdir"):
    INDEX_EXISTS = False
else:
    INDEX_EXISTS = True
    ix = open_dir("indexdir")

def get_spelling_suggestions(searcher, query_text):
    """Generate spelling suggestions for search terms"""
    if not query_text.strip():
        return []
        
    corrector = searcher.corrector("symptoms")
    suggestions = []
    for word in query_text.split():
        if len(word) > 2:  # Only suggest for words longer than 2 characters
            suggestions.extend(corrector.suggest(word, limit=2))
    return list(set(suggestions))[:3]  # Return top 3 unique suggestions

def get_related_symptoms(searcher, results):
    """Extract related symptoms from search results"""
    related = set()
    for hit in results:
        for term in hit.matched_terms():
            if term[0] == "symptoms":
                related.add(term[1].decode('utf-8'))
    return related

@app.route("/", methods=["GET", "POST"])
def search():
    error_message = None
    results = None
    query_text = ""
    suggestions = []
    related_terms = set()
    search_performed = False
    ir_method = "BM25F"
    
    if not INDEX_EXISTS:
        error_message = "Database index not found. Please run 'python index_data.py' first to create the index."
        return render_template("search.html", error=error_message)
    
    try:
        if request.method == "POST":
            query_text = request.form.get("symptoms", "").strip()
            search_performed = True
            
            if not query_text:
                error_message = "Please enter symptoms to search"
                return render_template("search.html", error=error_message)
                
            # Create searcher with BM25F scoring
            searcher = ix.searcher(weighting=BM25F(B=0.75, K1=1.5))
            
            # Setup query parser with fuzzy matching
            parser = MultifieldParser(["symptoms", "synonyms"], 
                                     schema=ix.schema, 
                                     group=OrGroup.factory(0.9))
            parser.add_plugin(FuzzyTermPlugin())
            query = parser.parse(query_text)
            
            # Get spelling suggestions
            suggestions = get_spelling_suggestions(searcher, query_text)
            
            # Perform search with highlighted results
            results = searcher.search(query, limit=10, terms=True)
            results.formatter.fragment_size = 50  # Set fragment size for highlighting
            
            # Get related symptoms
            related_terms = get_related_symptoms(searcher, results)
            
            # IR method explanation
            ir_method = "BM25F (Best Match 25 with Field weights)"
            
            if not results:
                error_message = f"No matches found for '{query_text}'. Try different symptoms or check suggested terms."
    
    except Exception as e:
        error_message = f"Search error: {str(e)}"
        print(traceback.format_exc())
    
    return render_template("search.html", 
                          results=results,
                          query=query_text,
                          suggestions=suggestions,
                          related_terms=related_terms,
                          search_performed=search_performed,
                          error=error_message,
                          ir_method=ir_method)

@app.route("/about")
def about():
    """About page with information about the application"""
    return render_template("about.html")

@app.route("/api/suggest", methods=["POST"])
def suggest():
    """API endpoint for auto-suggestions"""
    if not INDEX_EXISTS:
        return jsonify({"suggestions": []})
        
    query_text = request.json.get("text", "").strip()
    if not query_text or len(query_text) < 2:
        return jsonify({"suggestions": []})
        
    searcher = ix.searcher()
    corrector = searcher.corrector("symptoms")
    suggestions = corrector.suggest(query_text, limit=5)
    
    return jsonify({"suggestions": suggestions})

if __name__ == "__main__":
    app.run(debug=True)