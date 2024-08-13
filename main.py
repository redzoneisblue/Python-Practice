import tkinter
import customtkinter
from pytube import YouTube
import threading

def startDownload():
    ytlink = url_var.get()
    if ytlink == "":
        status_label.configure(text="Please enter a YouTube link.")
        return

    def download_video():
        try:
            ytObject = YouTube(ytlink)
            print(f"Title: {ytObject.title}")  # Debug: Print the title of the video
            video = ytObject.streams.get_highest_resolution()
            video.download()
            status_label.configure(text="Download complete.")
        except Exception as e:
            print(f"Error: {str(e)}")  # Debug: Print the error
            status_label.configure(text=f"Error: {str(e)}")

    # Start download in a separate thread to keep the UI responsive
    download_thread = threading.Thread(target=download_video)
    download_thread.start()

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=20, pady=20)

# Status label
status_label = customtkinter.CTkLabel(app, text="")
status_label.pack(padx=10, pady=10)

# Run app
app.mainloop()
