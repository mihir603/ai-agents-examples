def ask_gemini(user_message):
  response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[{"role": "system",
                   "content": "You are a helpful assistant."},
                  {"role": "user", "content": user_message}],
        temperature=0.7,
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "recommend",
                    "description": "Provide a … topic.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "topic": {
                                "type": "string",
                                "description": 
                                   "The topic,… for.",
                            },
                            "rating": {
                                "type": "string",
                                "description": 
                          "The rating … given.",
                                "enum": ["good",
                                         "bad", 
                                         "terrible"]
                                },
                        },
                        "required": ["topic"],
                    },
                },
                }
            ]
        )

user = "Can you please recommend me a time travel movie?"
response = ask_gemini(user)     
print(response)