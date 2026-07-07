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
            "reply": "Enjoy your movie! Have a great time.",
            "memory_update": {
                "personality": [],
                "events": [],
                "hobbies": []
            }
        }

    elif "birthday" in message:
        return {
            "reply": "Happy Birthday! Hope you have a wonderful day with your family and friends.",
            "memory_update": {
                "personality": [],
                "events": [],
                "hobbies": []
            }
        }

    elif "meeting" in message:
        return {
            "reply": "You have an upcoming meeting. Make sure to review your agenda and join on time.",
            "memory_update": {
                "personality": [],
                "events": [],
                "hobbies": []
            }
        }

    elif "study" in message:
        return {
            "reply": "Create a study schedule, focus on one topic at a time, and take short breaks between sessions.",
            "memory_update": {
                "personality": [],
                "events": [],
                "hobbies": []
            }
        }

    elif "gym" in message or "exercise" in message:
        return {
            "reply": "A 30-minute workout followed by proper hydration is a great choice today.",
            "memory_update": {
                "personality": [],
                "events": [],
                "hobbies": []
            }
        }

    elif "travel" in message or "trip" in message:
        return {
            "reply": "Have a safe trip! Don't forget to carry your essentials and check your travel schedule.",
            "memory_update": {
                "personality": [],
                "events": [],
                "hobbies": []
            }
        }

    elif "hello" in message or "hi" in message:
        return {
            "reply": "Hello! How can I help you today?",
            "memory_update": {
                "personality": [],
                "events": [],
                "hobbies": []
            }
        }

    elif "thank" in message:
        return {
            "reply": "You're welcome! Happy to help.",
            "memory_update": {
                "personality": [],
                "events": [],
                "hobbies": []
            }
        }

    else:
        return {
            "reply": "I'm here to help you. Could you please tell me more?",
            "memory_update": {
                "personality": [],
                "events": [],
                "hobbies": []
            }
        }