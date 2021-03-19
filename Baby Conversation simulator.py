from random import choice

questions=["Why is sky blue?: ",  "Why do stars twinkle?:" ,"Where are all the dinosaurs?:",
                    "Why there is face on moon?:"]

question=choice(questions)
answer=input(question).strip().lower()

while answer!="just because":
    answer=input("Why?? ").strip().lower()

