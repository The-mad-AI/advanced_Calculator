books = [
    {"title": "Atomic Habits", "rating": 4.8},
    {"title": "The Achemist", "rating": 3.9},
    {"title": "Deep Work", "rating": 4.5},
    {"title": "The Subtle Art of Not Giving a fuck", "rating":4.0},
    {"title": "Rich Dad Poor Dad", "rating":3.5}
]


filtered_books = list(filter(lambda b: b["rating"] > 4 , books))
percent_ratings = list(map(lambda b: {"title": b["title"],"percent": b["rating"] * 20 },fiilterd_books))

for book in percent_ratings:
    print(f"{book['title']}:{book['percent']}%")