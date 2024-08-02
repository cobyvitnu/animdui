from your_module import get_scraper_info

def get_scraper_info(field_type_id):
    scraper = get_scraper_info(field_type_id)
    if scraper:
        return scraper.info
    else:
        return None
