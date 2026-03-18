from duckduckgo_search import DDGS

def web_search(query: str, max_results: int = 3) -> str:
    """
    Perform a web search and return summarized results.
    """
    results = []

    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append(r.get("body", ""))
    except Exception as e:
        return f"Web search error: {e}"

    return "\n".join(results)