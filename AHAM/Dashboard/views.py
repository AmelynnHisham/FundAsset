import os
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from datetime import datetime

def dashboard(request):
    view_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(view_dir, 'portfolio.json')

    total_investments = 0  # Initialize the total investments

    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        for item in data:
            total = 0
            if 'transactions' in item:
                for value in item["transactions"]:
                    amount = value["amount"]
                    unit = value["unit"]
                    total += float(amount) * float(unit)
                item["total"] = total # Total value per fund
                total_investments += total  # All fund's total as total_investments

        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    except FileNotFoundError:
        print("failed")
        data = []

    return render(request, "index.html", {'data': data, 'total_investments': total_investments})


def fundDetail(request, id):
    view_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(view_dir, 'portfolio.json')

    if request.method == "GET":
        try:
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)
            
            for item in data:
                # Match the ID from row clicked
                if str(item.get("id")) == id:
                    return render(request, "fundDetail.html", {'item': item})

        except FileNotFoundError:
            print("failed")
            data = {}

    return render(request, "fundDetail.html", {'data': data})

def addFund(request, id):
    if request.method == "POST":
        view_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(view_dir, 'portfolio.json')

        if request.method == "POST":
            try:
                with open(json_file_path, 'r') as json_file:
                    data = json.load(json_file)
                
                for item in data:
                    if str(item.get("id")) == id:
                        created_at = datetime.now().strftime("%#d %b %Y")
                        amount = float(request.POST.get('amount'))
                        unit = float(request.POST.get('unit'))
                        
                        new_data = {
                            "created_at": created_at,
                            "amount": amount,
                            "unit": unit,
                        }

                        item["transactions"].append(new_data)
                        print(data)
                        
                with open(json_file_path, 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                
                return JsonResponse({"result": "success"})

            except FileNotFoundError:
                print("failed")
                data = {}
                     
        return JsonResponse({"result": "error"})

def allFunds(request):
    view_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(view_dir, 'funds.json')

    context = {}

    if request.method == "GET":
        try:
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)

        except FileNotFoundError:
            print("failed")
            data = {}
        
        context = {
            'data': data
        }

    return render(request, "allFunds.html", context)

def transactions(request):
    view_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(view_dir, 'portfolio.json')

    context = {}

    if request.method == "GET":
        try:
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)

        except FileNotFoundError:
            print("failed")
            data = {}
        
        context = {
            'data': data
        }

    return render(request, "transactions.html", context)

def performance(request):
    return render(request, "performance.html", {})