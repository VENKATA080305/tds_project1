import sqlite3

def calculate_gold_ticket_sales():
    """Calculates total sales for 'Gold' category tickets in an SQLite database"""
    try:
        conn = sqlite3.connect("/data/tickets.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT SUM(price) FROM tickets WHERE category = 'Gold'")
        total_sales = cursor.fetchone()[0] or 0
        
        conn.close()
        return {"status": "Gold ticket sales calculated", "total_sales": total_sales}, 200
    except Exception as e:
        return {"error": f"Failed to calculate sales: {str(e)}"}, 500
