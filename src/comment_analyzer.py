import json
from .file_handler import read_file, write_file

def find_similar_comments_task():
    """Finds similar comments using simple text matching"""
    try:
        comments = json.loads(read_file("/data/comments.json"))
        
        def calculate_similarity(text1, text2):
            """Calculate a simple similarity score based on common words"""
            words1 = set(text1.lower().split())
            words2 = set(text2.lower().split())
            common_words = len(words1.intersection(words2))
            total_words = len(words1.union(words2))
            return common_words / total_words if total_words > 0 else 0
        
        similar_comments = []
        for i, comment in enumerate(comments):
            max_similarity = 0
            most_similar = comment["text"]
            
            for j, other_comment in enumerate(comments):
                if i != j:
                    similarity = calculate_similarity(comment["text"], other_comment["text"])
                    if similarity > max_similarity:
                        max_similarity = similarity
                        most_similar = other_comment["text"]
            
            similar_comments.append({
                "comment": comment["text"],
                "similar_to": most_similar,
                "similarity_score": max_similarity
            })

        write_file("/data/similar_comments.json", json.dumps(similar_comments, indent=4))
        return {"status": "Most similar comments identified"}, 200
    except Exception as e:
        return {"error": f"Failed to find similar comments: {str(e)}"}, 500