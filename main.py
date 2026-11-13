import os

JOKE = (
    "My AI agent finished my ticket in 30 seconds, "
    "then spent three hours asking me why its code doesn't work. "
    "I used to talk to a rubber duck. "
    "Now the duck talks back \u2014 and it charges by the token."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
