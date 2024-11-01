class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def search_contact(self, search_term):
        # Search logic here
        pass

    def update_contact(self, name):
        # Update logic here
        pass

    def delete_contact(self, name):
        # Delete logic here
        pass
