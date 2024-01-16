class User:
    def __init__(self, user_email, user_name, password, current_job_title):        #constructor function to initialize class
        self.email = user_email
        self.name = user_name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):                    #function to change password
        self.password = new_password
    

    def change_job_title(self, new_job_title):                 #function to change job title
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}.")

