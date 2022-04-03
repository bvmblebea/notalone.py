import requests


class NotAloneClient:
    def __init__(self):
        self.api = "https://api.notalone.tv"
        self.api_key = "odsu6JggH90Z1D69AVCw"
        self.token = None
        self.user_id = None
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"}

    def login(self, login: str, password: str):
        data = {
            "apiKey": self.api_key,
            "login": login,
            "password": password
        }
        request = requests.post(
            f"{self.api}/auth",
            data=data,
            headers=self.headers)
        response = request.json()
        self.token = response["data"]["token"]
        self.user_id = response["data"]["id"]
        return response

    def register(
            self,
            login: str,
            email: str,
            password: str,
            nickname: str,
            gender: str = "male"):
        data = {
            "apiKey": self.api_key,
            "login": login,
            "email": email,
            "password": password,
            "nickname": nickname,
            "gender": gender
        }
        return requests.post(
            f"{self.api}/register",
            data=data,
            headers=self.headers).json()

    def get_user_info(self, user_id: int):
        data = {
            "apiKey": self.api_key,
            "userID": user_id
        }
        return requests.post(
            f"{self.api}/getUser",
            data=data,
            headers=self.headers).json()

    def get_user_rooms(self, user_id: int):
        data = {
            "apiKey": self.api_key,
            "userID": user_id
        }
        return requests.post(
            f"{self.api}/getUserRooms",
            data=data,
            headers=self.headers).json()

    def get_user_favorites(self, user_id: int, status: int = 0, page: int = 1):
        data = {
            "apiKey": self.api_key,
            "userID": user_id,
            "status": status,
            "page": page
        }
        return requests.post(
            f"{self.api}/getUserFavorites",
            data=data,
            headers=self.headers).json()

    def get_catalog(
            self,
            page: int = 1,
            category: str = "anime",
            genres: str = "детектив,боевик",
            years: str = "2010,2022"):
        data = {
            "apiKey": self.api_key,
            "page": page,
            "category": category,
            "genres": genres,
            "years": years
        }
        return requests.post(
            f"{self.api}/getCatalog",
            data=data,
            headers=self.headers).json()

    def get_catalog_item(self, item_id: int):
        data = {
            "apiKey": self.api_key,
            "itemID": item_id
        }
        return requests.post(
            f"{self.api}/getCatalogItem",
            data=data,
            headers=self.headers).json()

    def get_catalog_newest(self, page: int = 1):
        data = {
            "apiKey": self.api_key,
            "page": page
        }
        return requests.post(
            f"{self.api}/getCatalogNewest",
            data=data,
            headers=self.headers).json()

    def get_catalog_popular(self, page: int = 1):
        data = {
            "apiKey": self.api_key,
            "page": page
        }
        return requests.post(
            f"{self.api}/getCatalogPopular",
            data=data,
            headers=self.headers).json()

    def search_catalog(self, query: str):
        data = {
            "apiKey": self.api_key,
            "query": query
        }
        return requests.post(
            f"{self.api}/catalogSearch",
            data=data,
            headers=self.headers).json()

    def get_genres(self):
        data = {"apiKey": self.api_key}
        return requests.post(
            f"{self.api}/getGenres",
            data=data,
            headers=self.headers).json()

    def get_countries(self):
        data = {"apiKey": self.api_key}
        return requests.post(
            f"{self.api}/getCountries",
            data=data,
            headers=self.headers).json()
