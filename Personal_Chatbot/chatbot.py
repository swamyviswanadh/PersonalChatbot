
import os
import requests


class chat:
    def __init__(self):
        pass

    def bot(self,prompt):
        API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"
        headers = {"Authorization":"Bearer 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",}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        response = query({
            "messages": [
                {
                    "role": "user",
                    "content": "What is the capital of France?"
                }
            ],
            "model": "minimaxai/minimax-m1-80k"
        })
        rs=response["choices"][0]["message"]["content"]
        idx=rs.index("/think")+7
        rs=rs[idx:]
        return rs
        