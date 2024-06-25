from tech_news.database import db


# Requisito 10
def top_5_categories():
    pipeline = [
        {"$unwind": "$category"},
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5}
    ]
    
    categories = list(db.news.aggregate(pipeline))
    
    top_categories = [category["_id"] for category in categories]
    
    return top_categories
