import tkinter as tk
from tkinter import messagebox
import datetime

class BankingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("VMT Bank")
        self.geometry("400x300")

        self.current_balance = 0  
        self.my_account_number = "INDAVS0011092004"
        self.transactions = []  

        self.notification_var = tk.StringVar()
        self.notification_var.set("") 

        self.login_page()

    def login_page(self):
        self.clear_widgets()
        self.label = tk.Label(self, text="Hello! Welcome to VMT bank!\nPlease login to proceed.")
        self.label.pack(pady=10)

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login_process)
        self.login_button.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def login_process(self):
        username = self.username_entry.get()
        password = self.password_entry.get()


        print(f"Logging in with username: {username}, password: {password}")

        
        self.main_menu()

    def main_menu(self):
        self.clear_widgets()
        self.label = tk.Label(self, text="Main Menu")
        self.label.pack(pady=10)

        self.deposit_button = tk.Button(self, text="Deposit", command=self.deposit_page)
        self.deposit_button.pack(pady=5)

        self.withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw_page)
        self.withdraw_button.pack(pady=5)

        self.transfer_button = tk.Button(self, text="Transfer", command=self.transfer_page)
        self.transfer_button.pack(pady=5)

        self.transaction_history_button = tk.Button(self, text="Transaction History", command=self.transaction_history_page)
        self.transaction_history_button.pack(pady=5)

        self.quit_button = tk.Button(self, text="Quit", command=self.on_closing)
        self.quit_button.pack(pady=5)

    def deposit_page(self):
        self.clear_widgets()
        self.label = tk.Label(self, text="Deposit Money")
        self.label.pack(pady=10)

        self.amount_label = tk.Label(self, text="Enter Amount:")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady=5)

        self.deposit_button = tk.Button(self, text="Deposit", command=self.deposit_cash)
        self.deposit_button.pack(pady=5)

        self.notification_label = tk.Label(self, textvariable=self.notification_var)
        self.notification_label.pack(pady=5)

        self.back_to_menu_button = tk.Button(self, text="Back to Menu", command=self.main_menu)
        self.back_to_menu_button.pack(pady=5)

    def deposit_cash(self):
        amount = self.amount_entry.get()

        if not amount.isdigit() or int(amount) < 0:
            self.show_notification("Enter a valid amount.")
        else:
            self.current_balance += int(amount)
            self.transactions.append(("Deposited", f"Rs: {amount}", self.my_account_number, datetime.datetime.now().strftime("%d/%m/%Y - %I:%M %p")))
            message = f"Amount of {amount} deposited successfully. Current balance: {self.current_balance}"
            self.show_notification(message)
            self.amount_entry.delete(0, 'end')  # Clear the amount entry

    def withdraw_page(self):
        self.clear_widgets()
        self.label = tk.Label(self, text="Withdraw Money")
        self.label.pack(pady=10)

        self.amount_label = tk.Label(self, text="Enter Amount:")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady=5)

        self.withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw_cash)
        self.withdraw_button.pack(pady=5)

        self.notification_label = tk.Label(self, textvariable=self.notification_var)
        self.notification_label.pack(pady=5)

        self.back_to_menu_button = tk.Button(self, text="Back to Menu", command=self.main_menu)
        self.back_to_menu_button.pack(pady=5)

    def withdraw_cash(self):
        amount = self.amount_entry.get()

        if not amount.isdigit() or int(amount) < 0:
            self.show_notification("Enter a valid amount.")
        elif int(amount) > self.current_balance:
            message = f"Enter an amount less than or equal to the current balance (Current balance: {self.current_balance})."
            self.show_notification(message)
        else:
            self.current_balance -= int(amount)
            self.transactions.append(("Withdrawn", f"Rs: {amount}", self.my_account_number, datetime.datetime.now().strftime("%d/%m/%Y - %I:%M %p")))
            message = f"Amount of {amount} withdrawn successfully. Current balance: {self.current_balance}"
            self.show_notification(message)
            self.amount_entry.delete(0, 'end')  

    def transfer_page(self):
        self.clear_widgets()
        self.label = tk.Label(self, text="Transfer Money")
        self.label.pack(pady=10)

        self.account_label = tk.Label(self, text="Enter Recipient's Account Number:")
        self.account_label.pack(pady=5)
        self.account_entry = tk.Entry(self)
        self.account_entry.pack(pady=5)

        self.amount_label = tk.Label(self, text="Enter Amount:")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady=5)

        self.transfer_button = tk.Button(self, text="Transfer", command=self.transfer_money)
        self.transfer_button.pack(pady=5)

        self.notification_label = tk.Label(self, textvariable=self.notification_var)
        self.notification_label.pack(pady=5)

        self.back_to_menu_button = tk.Button(self, text="Back to Menu", command=self.main_menu)
        self.back_to_menu_button.pack(pady=5)

    def transfer_money(self):
        recipient_account = self.account_entry.get()
        amount = self.amount_entry.get()

        if recipient_account == self.my_account_number:
            self.show_notification("You can't transfer funds to your own account.")
        elif len(recipient_account) != 16 or not recipient_account.isalnum():
            self.show_notification("Enter a valid 16-digit account number.")
        elif not amount.isdigit() or int(amount) < 0:
            self.show_notification("Enter a valid amount.")
        elif int(amount) > self.current_balance:
            message = f"Enter an amount less than or equal to the current balance (Current balance: {self.current_balance})."
            self.show_notification(message)
        else:
            self.current_balance -= int(amount)
            self.transactions.append(("Transferred", f"Rs: {amount} to {recipient_account}", self.my_account_number, datetime.datetime.now().strftime("%d/%m/%Y - %I:%M %p")))
            message = f"Amount of {amount} transferred to {recipient_account} successfully. Current balance: {self.current_balance}"
            self.show_notification(message)
            self.account_entry.delete(0, 'end') 
            self.amount_entry.delete(0, 'end') 

    def transaction_history_page(self):
        self.clear_widgets()
        self.label = tk.Label(self, text="Transaction History")
        self.label.pack(pady=10)

        if not self.transactions:
            self.transaction_table = tk.Label(self, text="No transactions made.")
            self.transaction_table.pack(pady=5)
        else:
            headers = ["Transaction Type", "Amount", "Account Number", "Date/Time"]
            self.transaction_table = tk.Label(self, text="\t\t".join(headers))
            self.transaction_table.pack()

            for transaction in self.transactions:
                transaction_info = "\t\t".join(map(str, transaction))
                row = tk.Label(self, text=transaction_info, justify=tk.LEFT)
                row.pack()

        self.back_to_menu_button = tk.Button(self, text="Back to Menu", command=self.main_menu)
        self.back_to_menu_button.pack(pady=5)

    def show_notification(self, message):
        self.notification_var.set(message)
        self.after(3000, self.clear_notification)

    def clear_notification(self):
        self.notification_var.set("")

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

if __name__ == "__main__":
    app = BankingApp()
    app.mainloop()
