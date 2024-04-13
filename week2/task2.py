def book(consultants, hour, duration, criteria):
    best_consultant = {}
    for consultant in consultants:
        available = True
        for booking in consultant.get("bookings", []):
            if (hour < booking["hour"] + booking["duration"] and hour + duration > booking["hour"]):
                available = False
                break
        if available:
            if criteria == "price":
                if (not best_consultant) or (consultant["price"] < best_consultant["price"]):
                    best_consultant = consultant
            elif criteria == "rate":
                if (not best_consultant) or (consultant["rate"] > best_consultant["rate"]):
                    best_consultant = consultant
    if best_consultant:
        print(best_consultant["name"])
        best_consultant.setdefault("bookings", []).append({"hour": hour, "duration": duration})
    else:
        print("No Service")

consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]

book(consultants, 15, 1, "price") # Jenny
print(consultants)
book(consultants, 11, 2, "price") # Jenny
print(consultants)
book(consultants, 10, 2, "price") # John
print(consultants)
book(consultants, 20, 2, "rate") # John
print(consultants)
book(consultants, 11, 1, "rate") # Bob
print(consultants)
book(consultants, 11, 2, "rate") # No Service
print(consultants)
book(consultants, 14, 3, "price") # John
print(consultants)
