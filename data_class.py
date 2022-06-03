import requests, json, urls


class Data:
    def __init__(self, pages: int):
        self.pages = pages

    def instant_data(self):
        """This method extracts multi-page instant data."""
        data_list = []
        for page in range(self.pages):
            raw_data = requests.get(urls.data_url(page)).text
            raw_list = json.loads(raw_data)
            data_list.append(raw_list)

        combined_list = []
        for item in data_list:
            combined_list.extend(item)

        return combined_list


class HData:
    def __init__(self, token_id: str, date: str):
        self.token_id = token_id
        self.date = date

    def historical_data(self):
        """This method extracts historical data by token ID and date."""
        data_list = []
        url = urls.historical_data_url(self.token_id, self.date)
        raw_data = requests.get(url).text
        raw_list = json.loads(raw_data)
        data_list.append(raw_list)

        return data_list
