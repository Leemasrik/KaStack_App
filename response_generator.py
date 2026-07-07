def generate_response(request):

    message = request.message.lower()

    if "exam" in message:
        return {
            "reply": "You have an OOPS exam tomorrow. Revise OOP concepts for two hours today.",

            "memory_update": {
                "personality": [],
                "events": [],
                "hobbies": []
            }
        }

    elif "movie" in message:
        return {
            "reply": "Enjoy your movie!",

            "memory_update": {
                "personality": [],
                "events": [],
                "hobbies": []
            }
        }

    else:
        return {
            "reply": "I'm here to help you.",

            "memory_update": {
                "personality": [],
                "events": [],
                "hobbies": []
            }
        }