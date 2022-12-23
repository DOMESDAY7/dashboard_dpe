from dash import html
import json

questionAnswer = []

with open("q&a.json", "r") as f:
    questionAnswer = json.load(f)
f.close()

faqContent = []
for qAndA in questionAnswer:
    faqContent.append(html.Details([
        html.Summary(qAndA["question"]),
        html.P(qAndA["answer"])
    ],className="card"))