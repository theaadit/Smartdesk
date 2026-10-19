from pathlib import Path
import shutil

folder = Path(r"C:\TEST FOR ORGANIZER")

images = 0
videos = 0
documents = 0
applications = 0
music = 0
code = 0
other = 0
failed = 0
skipped = 0

images_folder = folder / "Images"
videos_folder = folder / "Videos"
documents_folder = folder / "Documents"
applications_folder = folder / "Applications"
music_folder = folder / "Music"
code_folder = folder / "Code"
other_folder = folder / "Other"

folders = [
    images_folder, videos_folder, documents_folder,
    applications_folder, music_folder, code_folder, other_folder
]

for destination in folders:
    destination.mkdir(parents=True, exist_ok=True)

for item in folder.iterdir():
    
    if item.is_file():
        extension = item.suffix.lower()

        if extension in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
            destination = images_folder
            category = "images"
        elif extension in [".mp4", ".mkv", ".avi", ".mov"]:
            destination = videos_folder
            category = "videos"
        elif extension in [".pdf", ".doc", ".docx", ".txt"]:
            destination = documents_folder
            category = "documents"
        elif extension in [".exe", ".msi"]:
            destination = applications_folder
            category = "applications"
        elif extension in [".mp3", ".wav", ".flac"]:
            destination = music_folder
            category = "music"
        elif extension in [".py", ".c", ".cpp", ".java", ".js", ".html", ".css"]:
            destination = code_folder
            category = "code"
        else:
            destination = other_folder
            category = "other"

        new_file = destination / item.name

        if new_file.exists():
            print("Already organized, skipping:", item.name)
            skipped += 1
            continue
        try:
            shutil.copy2(str(item), str(new_file))
            print(f"Copied: {item.name} ---> {destination.name}")

            if category == "images":
                images += 1
            elif category == "videos":
                videos += 1
            elif category == "documents":
                documents += 1
            elif category == "applications":
                applications += 1
            elif category == "music":
                music += 1
            elif category == "code":
                code += 1
            else:
                other += 1

        except Exception as e:
            print(f"Failed: {item.name} | Reason: {e}")
            failed += 1

print("\n========== FILE REPORT ==========")
print("Images copied       :", images)
print("Videos copied       :", videos)
print("Documents copied    :", documents)
print("Applications copied :", applications)
print("Music copied        :", music)
print("Code copied         :", code)
print("Other copied        :", other)
print("Skipped             :", skipped)
print("Failed              :", failed)
print("=================================")