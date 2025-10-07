# Simple Log Analysis System
# Internship Project - Main Flow Services and Technologies

log_data = [
    "192.168.1.1 - GET /index.html 200",
    "192.168.1.2 - POST /login 404",
    "192.168.1.1 - GET /about.html 200",
    "192.168.1.3 - GET /contact.html 500",
    "192.168.1.1 - GET /index.html 200"
]

ip_count = {}
response_count = {}

for log in log_data:
    parts = log.split()
    ip = parts[0]
    response = parts[-1]

    ip_count[ip] = ip_count.get(ip, 0) + 1
    response_count[response] = response_count.get(response, 0) + 1

print("Most Frequent IP Address:")
print(max(ip_count, key=ip_count.get))

print("\nResponse Code Count:")
for code, count in response_count.items():
    print("Code", code, "appeared", count, "times")
