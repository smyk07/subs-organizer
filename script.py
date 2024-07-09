# Python Subtitle Organizer
# Places subtitle files found in the "Subs" or "Subtitles" folder for pirated seasons alongside episode's mkv or mp4 files...

# importing modules 
import os 
import shutil 

# checking for subtitles folder 
folders = os.listdir("./")
subs_path = None

# Check if a subs folder exists, if not, quit...
for folder in folders: 
    if folder == "Subs" or folder == "subs" or folder == "Subtitles" or folder == "subtitles":  
        subs_path = f"./{folder}"
        break  
    elif folder != "Subs" or folder != "subs" or folder != "Subtitles" or folder != "subtitles":  
        if folder == folders[len(folders)-1]: 
            print("No Detectable subtitle directory. Please try in a suitable directory.")
            quit() 
        else: 
            continue 

# getting episode folders within subs folder 
episodes = os.listdir(subs_path)

# running a for loop for each episode folder to detect a subtitle file and to copy the subtitle file to the root directory...
for episode in episodes: 
    # declare a variable of lists containing all subtitle files...
    sub_files = os.listdir(f"{subs_path}/{episode}/")

    # Choosing the language for the subtitle based on the name of the srt file (Only English For Now)...
    # For example, if there are multiple files named "1_English" and "2_English", "1_English" will be chosen as it comes first in the sub_files list...If an english srt file is not found, quit...
    sub_file = None
    for file in sub_files: 
        if file.endswith("_English.srt"): 
            sub_file = file
            break
        elif file.endswith("_English.srt") == False: 
            if file == sub_files[len(sub_files)-1]: 
                print("No English subtitle file found, exiting...")
                quit()
            else: 
                continue

    # Copies the subtitle file to the root directory
    shutil.copyfile(
        src = f"{subs_path}/{episode}/{sub_file}", 
        dst = f"./{episode}.srt", 
    )

    print(f"{episode} Successful...") 
