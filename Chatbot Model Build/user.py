class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.social_media_accounts = []

    def authenticate(self, entered_password):
        return self.password == entered_password

    def add_social_media_account(self, account):
        self.social_media_accounts.append(account)

    def update_profile(self, new_name=None, new_email=None):
        if new_name:
            self.name = new_name
        if new_email:
            self.email = new_email

    def display_info(self):
        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Social Media Accounts: {', '.join(self.social_media_accounts)}")
