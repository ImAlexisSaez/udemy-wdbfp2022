user_years = int(input("¿Cuántos años tienes? "))

user_months = user_years * 12
user_weeks = user_months * 52
user_days = user_weeks * 7
user_hours = user_days * 24
user_minutes = user_hours * 60
user_seconds = user_minutes * 60

print(f"Resulta que {user_years} años son, aproximadamente:")
print(f"\t{user_months} meses.")
print(f"\t{user_weeks} semanas.")
print(f"\t{user_days} días.")
print(f"\t{user_hours} horas.")
print(f"\t{user_minutes} minutos.")
print(f"\t{user_seconds} segundos.")
