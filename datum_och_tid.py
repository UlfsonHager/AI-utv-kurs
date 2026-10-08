from datetime import datetime

# Hämta aktuell datum och tid
nu = datetime.now()

# Skriv ut datum och tid
print(f"Dagens datum: {nu.strftime('%Y-%m-%d')}")
print(f"Aktuell tid: {nu.strftime('%H:%M:%S')}")
print(f"\nFullständig ttt information: {nu}")
