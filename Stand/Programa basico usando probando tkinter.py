import tkinter as tk
appbasica = tk.Tk()
appbasica.geometry("720x480")
appbasica.wm_title("Mi app basica")
appbasica.configure(
    background="Light Green",
    )
tk.Button(appbasica,
          text="Hola!",
          width=10,
          height=5
          ).pack(
            side="left"
          )
appbasica.mainloop()