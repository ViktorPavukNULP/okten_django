from rest_framework.views import APIView
from rest_framework.response import Response
import json


class UsersListCreateView(APIView):
    def get(self, *args, **kwargs):
        with open('./users.json') as f:
            users = json.load(f)
        return Response(users)

    def post(self, *args, **kwargs):
        user = self.request.data
        with open("users.json", "r+") as f:
            users = json.load(f)
            users.append(user)
            f.seek(0)
            json.dump(users, f)
        return Response('Created')
