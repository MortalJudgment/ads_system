from .db_connection import get_db_connection

class PGSearchTool:
    @staticmethod
    def search_ads(keywords, limit=5):
        query = """
        SELECT * FROM ads
        WHERE to_tsvector('english', description) @@ to_tsquery('english', %s)
        ORDER BY ts_rank(to_tsvector('english', description), to_tsquery('english', %s)) DESC
        LIMIT %s
        """
        search_term = ' & '.join(keywords)
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute(query, (search_term, search_term, limit))
            results = cur.fetchall()
        conn.close()
        return results

    @staticmethod
    def get_relevant_ads(user_interests, user_query, limit=3):
        # Combine user interests and query for better ad targeting
        combined_keywords = user_interests + user_query.split()
        return PGSearchTool.search_ads(combined_keywords, limit)