from src import read_conv_conf, overwrite_conv_conf, get_title_from_url, update_ydl_opts
import os
from youtube_dl import YoutubeDL

from tkinter import (
    StringVar,
    END,
    ttk,
    Button,
    Label,
    Entry,
    Menu,
    Tk,
    font,
    filedialog,
)

""" Dataclasses """
from dataclasses import dataclass


@dataclass
class OperatingSystem:
    system: str
    resolution_width: int
    resolution_height: int


@dataclass
class ConvConf:
    priority_format: str
    s_path: str


conv_conf = ConvConf(**read_conv_conf())
ydl_opts = update_ydl_opts(conv_conf.priority_format)

print(f"{ydl_opts=}")

audio_downloader = YoutubeDL(ydl_opts)
""" Read write dataclasses """

if conv_conf.priority_format == "wav":
    prior_format = ["wav", "mp3"]
else:
    prior_format = ["mp3", "wav"]

""" Constant design/layout values"""
spacer = 20
btn_width = 50
btn_height = 50


""" Main """


class GlobalSettings:
    def __init__(self, app) -> None:
        def open_path_select():
            conv_conf.s_path = (
                filedialog.askdirectory(title="Select save directory") + "/"
            )
            print(conv_conf.s_path)
            overwrite_conv_conf(conv_conf.__dict__)

        self.btn_save_path = Button(
            app,
            text="Select save directory",
            command=open_path_select,
            bg="#425A7D",
            fg="#DF7356",
        )
        self.btn_save_path.place(
            x=spacer, y=spacer, height=btn_height, width=6 * btn_width
        )

        self.format_dropdown = ttk.Combobox(values=prior_format)
        self.format_dropdown.current(0)
        self.format_dropdown.bind("<<ComboboxSelected>>", self.dropdown_callback)
        self.format_dropdown.place(
            x=6 * btn_width + 2 * spacer,
            y=spacer,
            width=2 * btn_width,
            height=btn_height,
        )

    def dropdown_callback(self, event=None):
        global audio_downloader
        if event:
            conv_conf.priority_format = self.format_dropdown.get()
            ydl_opts = update_ydl_opts(conv_conf.priority_format)
            audio_downloader = YoutubeDL(ydl_opts)
            print(f"Changes\n{conv_conf=}\n{ydl_opts=}")


class Labels:
    def __init__(self, app) -> None:
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Segoe Script", size=15, weight=font.BOLD)

        self.yt_link_paste = Label(
            app, text="Youtube link:", bg="#2A3240", fg="#DF7356", anchor="e"
        )
        self.yt_link_paste.place(
            x=0, y=2 * spacer + btn_height, height=btn_height, width=4 * btn_width
        )
        self.name_paste = Label(
            app, text="Song name:", bg="#2A3240", fg="#DF7356", anchor="e"
        )
        self.name_paste.place(
            x=0,
            y=3 * spacer + 2 * btn_height,
            height=btn_height,
            width=4 * btn_width,
        )

        self.export_name = Label(
            app, text="Export name:", bg="#2A3240", fg="#DF7356", anchor="e"
        )
        self.export_name.place(
            x=0,
            y=4 * spacer + 3 * btn_height,
            height=btn_height,
            width=4 * btn_width,
        )


class InputFieldsButtons:
    def __init__(self, app) -> None:
        self.entry_yt_link = Entry(app)
        self.entry_yt_link.place(
            x=spacer + 4 * btn_width,
            y=2 * spacer + btn_height,
            height=btn_height,
            width=11 * btn_width + spacer,
        )

        self.entry_song_name = Entry(app)
        self.entry_song_name.place(
            x=spacer + 4 * btn_width,
            y=3 * spacer + 2 * btn_height,
            height=btn_height,
            width=11 * btn_width + spacer,
        )

        self.run_yt_link = Button(
            app,
            text="Apply",
            command=self.apply_yt_link,
            bg="#425A7D",
            fg="#DF7356",
        )
        self.run_yt_link.place(
            x=2 * spacer + 15 * btn_width + spacer,
            y=2 * spacer + btn_height,
            height=btn_height,
            width=3 * btn_width,
        )
        self.run_yt_name = Button(
            app,
            text="Apply",
            command=self.apply_yt_name,
            bg="#425A7D",
            fg="#DF7356",
        )
        self.run_yt_name.place(
            x=2 * spacer + 15 * btn_width + spacer,
            y=3 * spacer + 2 * btn_height,
            height=btn_height,
            width=3 * btn_width,
        )
        self.entry_text = StringVar()
        self.export_name = Entry(app, textvariable=self.entry_text)
        self.export_name.place(
            x=spacer + 4 * btn_width,
            y=4 * spacer + 3 * btn_height,
            height=btn_height,
            width=11 * btn_width + spacer,
        )

        self.start_convert = Button(
            app,
            text="Convert",
            state="disabled",
            command=self.convert,
            bg="#425A7D",
            fg="#DF7356",
        )
        self.start_convert.place(
            x=2 * spacer + 15 * btn_width + spacer,
            y=4 * spacer + 3 * btn_height,
            height=btn_height,
            width=3 * btn_width,
        )

    def apply_yt_name(self):
        self.start_convert["state"] = "normal"
        print("TBD")

    def apply_yt_link(self):
        self.entry_text.set(get_title_from_url(self.entry_yt_link.get()))
        self.start_convert["state"] = "normal"

    def convert(self):
        print("converting...")
        self.start_convert["state"] = "disabled"

        info = audio_downloader.extract_info(self.entry_yt_link.get())

        os.rename(
            src=info["title"] + "-" + info["id"] + "." + conv_conf.priority_format,
            dst=conv_conf.s_path + self.export_name.get(),
        )
        print("\tFinished.")

        self.entry_yt_link.delete(0, END)
        self.entry_song_name.delete(0, END)
        self.export_name.delete(0, END)

    def show_entry_fields(self):
        print(
            "YT-link: %s\nYT-name: %s"
            % (self.entry_song_name.get(), self.entry_yt_link.get())
        )
        self.entry_yt_link.delete(0, END)
        self.entry_song_name.delete(0, END)


"""Main Init"""
app = Tk()
app.title("YouTube 2 Audio")
app.configure(background="#2A3240")  # Orange: #DF7356, Purple: #425A7D
app.grid()

global_settings = GlobalSettings(app)
input_fields = InputFieldsButtons(app)
dropdown = Menu(app)
datei_menu = Menu(dropdown, tearoff=0)

labels = Labels(app)
# datei_menu.add_command(label="Generate save folder", command=gen_save_folder)
datei_menu.add_separator()
datei_menu.add_command(label="Exit", command=app.quit)
dropdown.add_cascade(label="File", menu=datei_menu)


app.config(menu=dropdown)
app.geometry("1000x400")
app.mainloop()
