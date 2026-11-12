import re
contacts = [
    {
        "name": "Dr. Ravi",
        "phone": "+91 98400 12345",
        "email": "ravi@gmail.com"
    },
    {
        "name": "Ravi Kumar",
        "phone": "9840012345",
        "email": "ravi@gmail.com"
    },
    {
        "name": "Priya",
        "phone": "9876543210",
        "email": "priya@gmail.com"
    },
    {
        "name": "Arun",
        "phone": "9123456780",
        "email": "arun@gmail.com"
    }
]
merged = {}
for contact in contacts:
    phone = re.sub(r'\D', '', contact["phone"])
    if phone.startswith("91") and len(phone) == 12:
        phone = phone[2:]
    if phone not in merged:
        merged[phone] = {
            "name": contact["name"],
            "phones": set(),
            "emails": set()
        }
    merged[phone]["phones"].add(contact["phone"])
    if contact["email"]:
        merged[phone]["emails"].add(contact["email"])
print("Merged Contacts:")
for phone, details in merged.items():
    print("Name:", details["name"])
    print("Phone Numbers:", sorted(details["phones"]))
    print("Email Addresses:", sorted(details["emails"]))
    print()
