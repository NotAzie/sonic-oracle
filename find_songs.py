"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
# Allowed YouTube Category IDs: 10 (Music), 24 (Entertainment)
ALLOWED_CATEGORIES = {"10", "24"}

def is_valid_category(cat_id):
    if not cat_id:
        return True
    return str(cat_id) in ALLOWED_CATEGORIES
