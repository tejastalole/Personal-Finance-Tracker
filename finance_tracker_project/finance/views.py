from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from bson import ObjectId
import json

from .db import transactions_collection


# ✅ Custom serializer for ObjectId
class MongoJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)


# ✅ Get all transactions
def get_transactions(request):
    transactions = list(transactions_collection.find())
    for t in transactions:
        t["_id"] = str(t["_id"])  # Convert ObjectId -> string
    return JsonResponse(transactions, safe=False)


# ✅ Add transaction
@csrf_exempt
def add_transaction(request):
    if request.method == "POST":
        body = json.loads(request.body)
        transactions_collection.insert_one(body)
        return JsonResponse({"message": "Transaction added successfully"})
    return JsonResponse({"error": "Invalid request"}, status=400)


# ✅ Delete transaction
@csrf_exempt
def delete_transaction(request, id):
    transactions_collection.delete_one({"_id": ObjectId(id)})
    return JsonResponse({"message": "Transaction deleted successfully"})


# ✅ Render frontend page
def home(request):
    return render(request, "index.html")
