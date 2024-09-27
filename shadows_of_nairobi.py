import tkinter as tk
from tkinter import messagebox

class ShadowsOfNairobi:
    def __init__(self, root):
        self.root = root
        self.root.title("Shadows of Nairobi")
        self.root.geometry("600x400")

        # Create a text box for the storyline
        self.story_text = tk.Text(root, wrap="word", height=15, width=60)
        self.story_text.pack(pady=10)

        # Create buttons for choices
        self.choice_button1 = tk.Button(root, text="", command=self.choice1)
        self.choice_button2 = tk.Button(root, text="", command=self.choice2)

        self.choice_button1.pack(pady=5)
        self.choice_button2.pack(pady=5)

        # Initialize the game
        self.intro()

    def update_story(self, text, button1_text, button2_text):
        self.story_text.delete(1.0, tk.END)  # Clear the previous text
        self.story_text.insert(tk.END, text)  # Insert the new story text
        self.choice_button1.config(text=button1_text)  # Update button text
        self.choice_button2.config(text=button2_text)

    def game_over(self):
        messagebox.showinfo("Game Over", "You lose!")
        self.root.quit()

    def intro(self):
        text = ("Welcome to 'Shadows of Nairobi'.\n"
                "You are Detective Malik, hired to investigate a string of mysterious disappearances in Nairobi.\n"
                "Will you navigate the dangerous web of corruption, crime, and deception to solve the case?\n"
                "Your choices will determine your fate.")
        self.update_story(text, "Start Investigation", "")

    def first_choice(self):
        text = ("It’s a late evening. You receive a call from an unknown number. The voice on the other side says:\n"
                "'Detective Malik, if you want to stop the disappearances, meet me at Java Coffee on Kimathi Street in 30 minutes.'\n"
                "What do you do?")
        self.update_story(text, "Go to the meeting", "Ignore the call")

    def choice1(self):
        # Choice 1: The first button is clicked
        current_text = self.choice_button1.cget("text")
        if current_text == "Start Investigation":
            self.first_choice()
        elif current_text == "Go to the meeting":
            self.meeting_scene()
        elif current_text == "Press for more information":
            self.press_for_info()
        elif current_text == "Visit the businessman’s house":
            self.businessman_house()
        elif current_text == "Search the house for clues":
            self.search_house()
        elif current_text == "Enter the code: 3258":
            self.enter_safe_code() 
        elif current_text == "Visit the bar":
            self.visit_bar()       
        elif current_text == "Pay for information":
            self.pay_kioni()
        elif current_text == "Expose the truth":
            self.good_ending()
        elif current_text == "Play Again":
            self.intro()

    def choice2(self):
        # Choice 2: The second button is clicked
        current_text = self.choice_button2.cget("text")
        if current_text == "Ignore the call":
            self.ignore_meeting()
        elif current_text == "Take the folder and leave quietly":
            self.leave_coffee_shop()        
        elif current_text == "Call the police":
            self.call_police()
        elif current_text == "Visit the bar":
            self.visit_bar()
        elif current_text == "Threaten for information":
            self.threaten_kioni()
        elif current_text == "Use the information for blackmail":
            self.bad_ending()
        elif current_text == "Play Again":
            self.intro()

    def meeting_scene(self):
        text = ("You arrive at the coffee shop and find a man sitting in the corner, face hidden beneath a hat.\n"
                "He slides a folder across the table and says, 'This case runs deeper than you think.'\n"
                "What do you do next?")
        self.update_story(text, "Press for more information", "Take the folder and leave quietly")

    def press_for_info(self):
        text = ("The man looks around nervously. 'You don't understand. The more you know, the more danger you're in.'\n"
                "Before you can respond, he bolts out the door.\n"
                "You decide to look into the photos and start by visiting one of the locations in the folder.")
        self.update_story(text, "Visit the businessman’s house", "Visit the bar")

    def leave_coffee_shop(self):
        text = ("You take the folder and leave the coffee shop. Outside, you see a black car watching you from across the street.\n"
                "You feel like you're being followed, but decide to head home to review the information in the folder.\n"
                "What will you do next?")
        self.update_story(text, "Visit the businessman’s house", "Visit the bar")

    def ignore_meeting(self):
        text = ("You ignore the call and continue with your night. Days later, another disappearance happens, one you could have prevented.\n"
                "You can no longer ignore the case.")
        self.update_story(text, "Visit the businessman’s house", "Visit the bar")

    def businessman_house(self):
        text = ("You arrive at the businessman’s mansion. The gate is unlocked, and the house is eerily quiet.\n"
                "You find signs of a struggle inside, including a broken vase.\n"
                "Do you:")
        self.update_story(text, "Search the house for clues", "Call the police and report the scene")

    def search_house(self):
        text = ("While searching the house, you find a hidden safe behind a painting.\n"
                "It’s locked with a combination. The code you found in the folder is: 3258.\n"
                "What will you do?")
        self.update_story(text, "Enter the code: 3258", "Leave the house")

    def enter_safe_code(self):
        text = ("You enter the code and the safe clicks open. Inside, you find documents linking the businessman to a powerful political figure.\n"
                "It seems the disappearances are connected to something much bigger.\n"
                "What will you do next?")
        self.update_story(text, "Visit the bar", "")

    def call_police(self):
        text = ("You call the police, but they don’t take your report seriously. Frustrated, you decide to investigate further on your own.\n"
                "Where will you go?")
        self.update_story(text, "Visit the bar", "")

    def visit_bar(self):
        text = ("You arrive at the bar in Eastlands. The place is dimly lit, and the patrons eye you suspiciously.\n"
                "You find Kioni, a street informant, sitting in the corner. She knows everything about the underworld, but her information comes at a price.\n"
                "Do you:")
        self.update_story(text, "Pay for information", "Threaten for information")

    def pay_kioni(self):
        text = ("You slip Kioni some cash. She smirks and tells you that a high-ranking official is involved in the disappearances.\n"
                "She warns you to be careful, as the people behind this won’t hesitate to silence anyone who gets too close.\n"
                "You now have enough evidence to take down the people responsible.\n"
                "What will you do?")
        self.update_story(text, "Expose the truth", "Use the information for blackmail")

    def threaten_kioni(self):
        text = ("You lean in, your voice low and menacing. 'Tell me what you know, or things will get ugly.'\n"
                "Kioni laughs, unimpressed. 'You’re brave, detective, but you’re out of your league.' She gives you nothing.\n"
                "You now have enough evidence to take down the people responsible.\n"
                "What will you do?")
        self.update_story(text, "Expose the truth", "Use the information for blackmail")

    def final_decision(self):
        text = ("You now have enough evidence to take down the people responsible for the disappearances.\n"
                "But exposing them will put you and those close to you in danger.\n"
                "What will you do?")
        self.update_story(text, "Expose the truth", "Use the information for blackmail")

    def good_ending(self):
        text = ("You decide to expose the truth. The public is shocked as the scandal unfolds, and justice is served.\n"
                "Though it comes at a personal cost, you remain true to your principles.\n"
                "Congratulations, Detective Malik. You solved the case and brought the culprits to justice!")
        self.update_story(text, "Play Again", "")

    def bad_ending(self):
        text = ("You choose to blackmail the powerful figures involved. With the money and influence you gain, your life becomes comfortable.\n"
                "But the disappearances continue, and deep down, you know you’ve crossed a line you can never come back from.\n"
                "You solved the case, but at what cost, Detective Malik?")
        self.update_story(text, "Play Again", "")

# Main Program to start the game
root = tk.Tk()
game = ShadowsOfNairobi(root)
root.mainloop()
