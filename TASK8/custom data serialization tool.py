# --------------------------------------------------
# Project: Custom Data Serialization Tool
# Internship: Main Flow Services and Technologies
# --------------------------------------------------

# Function to serialize (convert dictionary to a single string)
def serialize(data):
    result = ""
    for key, value in data.items():
        result += f"{key}={value}|"
    return result[:-1]  # remove last '|'

# Function to deserialize (convert string back to dictionary)
def deserialize(serialized_str):
    data = {}
    items = serialized_str.split("|")
    for item in items:
        key, value = item.split("=")
        data[key] = value
    return data

# Example dictionary data
user_data = {
    "name": "Kiran",
    "age": "22",
    "city": "Hyderabad",
    "course": "Python Internship"
}

# Serialize and Deserialize
serialized_text = serialize(user_data)
print("Serialized Data:", serialized_text)

deserialized_data = deserialize(serialized_text)
print("Deserialized Data:", deserialized_data)
