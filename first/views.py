from rest_framework.views import APIView
from rest_framework.response import Response
import json


class UsersListCreateView(APIView):
    def get(self, *args, **kwargs):
        try:
            with open('./users.json') as f:
                users = json.load(f)
        except FileNotFoundError:
            return Response('File not found')
        return Response(users)

    def post(self, *args, **kwargs):
        user = self.request.data
        try:
            with open("users.json", "r+") as f:
                users = json.load(f)
                users.append(user)
                f.seek(0)
                json.dump(users, f)
        except FileNotFoundError:
            return Response('File not found')
        return Response('Created')
