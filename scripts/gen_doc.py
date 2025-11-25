# scripts/gen_doc.py
import os

print("Running gen_doc.py ...")
print("GITHUB_REPOSITORY:", os.getenv("GITHUB_REPOSITORY"))
print("GITHUB_ACTOR:", os.getenv("GITHUB_ACTOR"))
print("GITHUB_EVENT_NAME:", os.getenv("GITHUB_EVENT_NAME"))

