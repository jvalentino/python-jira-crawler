import requests



class UrlUtil:
    def __init__(self):
        pass

    def http_get(url, auth_token):
        headers = {
            "Authorization": auth_token
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    
    def http_get_pagination(url, auth_token, max_results=50, iteration_field='issues'):
        start_at = 0
        all_issues = []

        while True:
            extended_url = f"{url}&startAt={start_at}&maxResults={max_results}"
            print(f"   Fetching {extended_url}")
            response = UrlUtil.http_get(extended_url, auth_token)
            
            issues = response.get(iteration_field, [])
            if issues.__len__() == 0:
                break
            
            print(f"   Found {len(issues)} issues")
            all_issues.extend(issues)
            start_at += max_results

        return all_issues
