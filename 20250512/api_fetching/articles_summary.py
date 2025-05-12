from ask_ai import ask_ai

# Loop all files from the articles folder
import os, datetime

for filename in os.listdir("articles"):
    if filename.endswith(".txt"):
        # Read the file
        with open(f"articles/{filename}", "r", encoding="utf-8") as file:
            content = file.read()

        # Ask AI for a summary
        summary = ask_ai(f"Please conclude this news with points in Tradition Chinese in markdown:\n{content}")
        
        # Ask AI for a file name
        file_name = ask_ai(f"Please give a suitable title name for this news in Traditional Chinese, with format 'YYYY-MM-DD-<THE TITLE YOU GAVE>', if you can find the date of the acticle from the acticle, then use the date from the acticle, otherwise return the title name only without date:\n{content}").strip()

        # Check if the file name not starts with a date
        if not file_name.startswith("20"):
            # Get the current date
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            # Prepend the current date to the file name
            file_name = f"{current_date}-{file_name}"

        # Create the directory if it doesn't exist
        os.makedirs("articles_summaries", exist_ok=True)

        # Save the summary to a new file as markdown
        summary_filename = f"{file_name}.md"
        with open(f"articles_summaries/{summary_filename}", "w", encoding="utf-8") as file:
            file.write(summary)