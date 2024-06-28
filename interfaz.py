import tkinter as tk
from tkinter import ttk

class AudioCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Captura")
        self.root.geometry("300x600")

        self.is_playing = False

        # Título
        title_label = tk.Label(root, text="Captura", font=("Helvetica", 24))
        title_label.pack(pady=20)

        # Subtítulo
        subtitle_label = tk.Label(root, text="Acerca el dispositivo lo suficiente a la fuente de audio", font=("Helvetica", 12), fg="green")
        subtitle_label.pack(pady=10)

        # Área de captura de audio
        self.audio_frame = tk.Frame(root, bg="lightgreen", width=200, height=200)
        self.audio_frame.pack(pady=20)
        self.audio_frame.pack_propagate(False)

        self.audio_label = tk.Label(self.audio_frame, text="0:30 seg", font=("Helvetica", 14), bg="lightgreen")
        self.audio_label.pack(expand=True)

        # Canvas para la animación de la señal
        self.canvas = tk.Canvas(self.audio_frame, width=200, height=100, bg="lightgreen")
        self.canvas.pack()

        # Botón de play
        self.play_button = tk.Button(self.audio_frame, text="Play", font=("Helvetica", 12), bg="white", width=10, command=self.toggle_play)
        self.play_button.pack()

        # Botón de aceptar
        accept_button = tk.Button(root, text="Aceptar", font=("Helvetica", 14), bg="black", fg="white", width=15)
        accept_button.pack(pady=20)

        # Barra de navegación inferior
        nav_frame = tk.Frame(root, bg="white", height=50)
        nav_frame.pack(side="bottom", fill="x")

        # Botones de navegación
        nav_buttons = ["Chat", "Trivia", "Capturar", "Wiki", "Historia"]
        for button in nav_buttons:
            nav_button = tk.Button(nav_frame, text=button, font=("Helvetica", 10), bg="white", borderwidth=0)
            nav_button.pack(side="left", expand=True, fill="both")

        self.signal_position = 0

    def toggle_play(self):
        if self.is_playing:
            self.is_playing = False
            self.play_button.config(text="Play")
        else:
            self.is_playing = True
            self.play_button.config(text="Pause")
            self.animate_signal()

    def animate_signal(self):
        if self.is_playing:
            self.canvas.delete("all")
            self.signal_position = (self.signal_position + 5) % 200
            self.canvas.create_line(self.signal_position, 10, self.signal_position, 90, fill="white", width=5)
            self.root.after(50, self.animate_signal)

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioCaptureApp(root)
    root.mainloop()

