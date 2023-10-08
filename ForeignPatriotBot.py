import tkinter as tk

# List of countries
countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
             "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
             "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei",
             "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic",
             "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba",
             "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
             "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia",
             "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
             "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica",
             "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait",
             "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania",
             "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
             "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique",
             "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria",
             "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea",
             "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis",
             "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia",
             "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
             "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
             "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
             "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
             "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia",
             "Zimbabwe"] #List of countries here

def submit():
    user_input = user_entry.get()
    chat_text.config(state=tk.NORMAL)
    chat_text.insert(tk.END, "You: " + user_input + "\n")

    # Check if user is a foreign exchange student
    if user_input.lower() == "yes":
        chat_text.insert(tk.END, "ChatBot: That's great! What country are you from?\n")
    elif user_input.lower() == "no":
        chat_text.insert(tk.END, "ChatBot: Have a nice day!\n")
        user_entry.delete(0, tk.END)
    else:
        # Check if user input is a valid country (case-insensitive)
        if user_input.lower() in [country.lower() for country in countries]:
            if user_input.lower() == "pakistan":
                chat_text.insert(tk.END, "ChatBot: You've selected Pakistan. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Pakistan Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/psa/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "india":
                chat_text.insert(tk.END, "ChatBot: You've selected India. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Indian Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/indianstudenta/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "afghanistan":
                chat_text.insert(tk.END, "ChatBot: You've selected Afghanistan. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Afghan Student Union", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/asu/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "bangladesh":
                chat_text.insert(tk.END, "ChatBot: You've selected Bangladesh. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Bengali Patriots Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/bdgsa/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "brazil":
                chat_text.insert(tk.END, "ChatBot: You've selected Brazil. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Brazilian Student Association (BRASA)", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/brasa/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "china":
                chat_text.insert(tk.END, "ChatBot: You've selected China. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Chinese Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/gmucsa/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "egypt":
                chat_text.insert(tk.END, "ChatBot: You've selected Egypt. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Egyptian Student Union", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/esu/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "iraq":
                chat_text.insert(tk.END, "ChatBot: You've selected Iraq. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Iraqi Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/gmuiraqiss/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "italy":
                chat_text.insert(tk.END, "ChatBot: You've selected Italy. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Italian Club at Mason", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/italianclub/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "japan":
                chat_text.insert(tk.END, "ChatBot: You've selected Japan. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Japanese Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/jsa/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "lebanon":
                chat_text.insert(tk.END, "ChatBot: You've selected Lebanon. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Lebanese Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/lsa/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "morocco":
                chat_text.insert(tk.END, "ChatBot: You've selected Morocco. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Moroccan American Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/masa/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "nepal":
                chat_text.insert(tk.END, "ChatBot: You've selected Nepal. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Nepalese Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/nsa/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "saudi arabia":
                chat_text.insert(tk.END, "ChatBot: You've selected Saudi Arabia. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Saudi Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/saudisa/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "somalia":
                chat_text.insert(tk.END, "ChatBot: You've selected Somalia. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Somali Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/somalisa/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "sri lanka":
                chat_text.insert(tk.END, "ChatBot: You've selected Sri Lanka. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Sri Lankan Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/srlsa/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "sudan":
                chat_text.insert(tk.END, "ChatBot: You've selected Sudan. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Sudanese Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/ssa/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "taiwan":
                chat_text.insert(tk.END, "ChatBot: You've selected Taiwan. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Taiwanese Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/tsa/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "turkey":
                chat_text.insert(tk.END, "ChatBot: You've selected Turkey. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Turkish Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/tsam/home/"))
                chat_text.insert(tk.END, "\n")
            if user_input.lower() == "vietnam":
                chat_text.insert(tk.END, "ChatBot: You've selected Vietnam. Here is a link to learn more: ")
                chat_text.tag_configure("link", foreground="blue", underline=True)
                chat_text.insert(tk.END, "Vietnamese Student Association", "link")
                chat_text.tag_bind("link", "<Button-1>", lambda event: open_link("https://mason360.gmu.edu/vsa/home/"))
                chat_text.insert(tk.END, "\n")
            else:
                chat_text.insert(tk.END, f"ChatBot: You've selected {user_input}.\n")
        else:
            chat_text.insert(tk.END, "ChatBot: That doesn't appear to be a valid country. Please try again.\n")

    chat_text.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)

# Function to open a link in the default web browser
def open_link(url):
    import webbrowser
    webbrowser.open_new(url)

# Create the main window
root = tk.Tk()
root.title("ChatBot")

# Set the dimensions of the window
root.geometry("800x600")  # Width x Height

frame = tk.Frame(root, bg="darkgreen", padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# Create a text widget for displaying the conversation
chat_text = tk.Text(frame, height=5, width=120, font=("Helvetica", 20))  # Set font size and style here
chat_text.pack()
chat_text.insert(tk.END, "ChatBot: Hello! Are you a foreign exchange student? (Answer with 'yes' or 'no')\n")
chat_text.config(state=tk.DISABLED)

# Create an entry widget for user input
user_entry = tk.Entry(frame, width=120, font=("Helvetica", 20))  # Set font size and style here
user_entry.pack()

# Create a button to submit user input
submit_button = tk.Button(frame, text="Submit", command=submit, font=("Helvetica", 12))  # Set font size and style here
submit_button.pack()

# Main loop to keep the GUI running
root.mainloop()
