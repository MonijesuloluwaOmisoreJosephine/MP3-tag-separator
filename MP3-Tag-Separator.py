from mutagen.easyid3 import EasyID3
import os
import shutil
import stat

def replace_separator(file_path, tags, current_separator, new_separator):
    try:
        # Remove read-only attribute if it exists
        if not os.access(file_path, os.W_OK):
            os.chmod(file_path, stat.S_IWRITE)
        
        audio = EasyID3(file_path)
        for tag in tags:
            if tag.lower() in audio:
                tag_value = audio[tag.lower()][0].replace(current_separator, new_separator)
                audio[tag.lower()] = tag_value
                audio.save()
                print(f"Updated {tag.lower()} tag in {file_path} replacing '{current_separator}' with '{new_separator}'")
            else:
                print(f"No {tag.lower()} tag found in {file_path}")
    except PermissionError:
        print(f"Permission denied: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_directories():
    while True:
        # Ask user for the tags, current separator, and the new separator
        tags_input = input("Enter the tags you want to replace the separator for (comma-separated, no spaces between the commas, e.g., 'artist,genre,composer'): ").strip().split(',')
        tags_input = [tag.strip() for tag in tags_input]  # Strip whitespace from each tag
        
        if 'done' in tags_input:
            print("Goodbye!")
            break
        
        current_separator = input("Enter the current separator (e.g., '/', ',', '|'): ").strip()
        if current_separator.lower() == 'done':
            print("Goodbye!")
            break
        
        new_separator = input("Enter the new separator you want to replace it with (e.g., ';', '-', '_'): ").strip()
        if new_separator.lower() == 'done':
            print("Goodbye!")
            break

        while True:
            directory_path = input("Enter the path to the directory containing your music files (or type 'done' to finish): ").strip()
            if directory_path.lower() == 'done':
                break
            
            if os.path.isdir(directory_path):
                for root, _, files in os.walk(directory_path):
                    for file in files:
                        if file.endswith('.mp3'):
                            file_path = os.path.join(root, file)
                            replace_separator(file_path, tags_input, current_separator, new_separator)
            else:
                print("The provided path is not a valid directory.")

# Start processing directories
process_directories()
