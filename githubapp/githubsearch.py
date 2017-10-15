import requests


class gitHubApi():
    """
    """

    def __init__(self, request):
        self.request = request
        self.basic_search_url = 'https://api.github.com/search/repositories?q=%s&sort=stars&order=desc&per_page=50'

    def github_search(self):
        """
        """
        search_q = self.request.POST.get('query')
        search_url = self.basic_search_url % search_q
        results = requests.get(search_url)
        out_dict = {"languages": "", "average_star": "", "results": [], "total": 0}
        search_result = []
        if results.status_code == 200:
            results_dict = results.json()
            total = results_dict["total_count"]
            count = 0
            total_star = 0
            all_language = []
            for rec in results_dict["items"]:
                rec_dict = {}
                count += 1
                rec_dict["sr_no"] = count
                total_star += rec["stargazers_count"]
                rec_dict["star"] = rec["stargazers_count"]
                rec_dict["language"] = rec["language"]
                if rec["language"] and rec["language"] not in all_language:
                    all_language.append(rec["language"])
                rec_dict["description"] = rec["description"]
                rec_dict["url"] = rec["html_url"]
                search_result.append(rec_dict)
            out_dict["results"] = search_result
            out_dict["languages"] = ", ".join(all_language)
            out_dict["average_star"] = total_star / count
            out_dict["total"] = total
        return out_dict
