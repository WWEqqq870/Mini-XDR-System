import requests

# هذا هو رابط الخادم المحلي
URL = "http://127.0.0.1:8000/ingest"

def send_event(device, process, severity="low"):
    payload = {"device": device, "process": process, "severity": severity}
    r = requests.post(URL, json=payload)
    print("Response:", r.status_code, r.text)

if __name__ == "__main__":
    send_event("kali-vm", "a", "high")
