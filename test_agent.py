import ollama

print("⏳ שולח בקשה למודל המקומי... אנא המתן...")

# פנייה למנוע של Ollama שרץ אצלך על המחשב
response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "תגיד 'הכל עובד בהצלחה!' בעברית ותסביר בקצרה מי אתה.",
        }
    ],
)

# הדפסת התשובה שהתקבלה מהמודל
print("\n🤖 תשובת ה-AI:")
print(response["message"]["content"])
